# Spacecraft Telemetry Router

from typing import List, Dict, Union, Optional

class TelemetryPacket:
    """Single telemetry packet"""
    def __init__(self, packet_id: int, satellite_id: int, priority: int,
                 size_kb: float, data: dict):
        self.packet_id = packet_id
        self.satellite_id = satellite_id
        self.priority = priority
        self.size_kb = size_kb
        self.data: dict = data
    
    def __lt__(self, other: "TelemetryPacket"):
        if self.priority != other.priority:
            return self.priority < other.priority
        else:
            return self.packet_id > other.packet_id
    
    def __repr__(self) -> str:
        return f"Packet(id={self.packet_id}, priority={self.priority}, size_kb={self.size_kb}, length_of_data={len(self.data)})"

class Spacecraft:
    def __init__(self, satellite_id: int, name: str, health: float,
                 downlink_rate_kbps: float, buffer: List[TelemetryPacket]):
        self.satellite_id = satellite_id
        self.name = name
        self.health = health
        self.downlink_rate_kbps = downlink_rate_kbps
        self.buffer = buffer
    
    def generate_packet(self, packet: TelemetryPacket):
        return self.buffer.append(packet)

    def pop_packets(self, max_kb: float) -> List[TelemetryPacket]:
        """Return a list of packets whose total size is less than max_kb"""
        fifo_packet_size = 0
        fifo_packets = []
        for idx, packet in enumerate(self.buffer):
            if idx == 0 and packet.size_kb > max_kb:  # Reject the first packet if its size is too large
                return []
            if fifo_packet_size + packet.size_kb <= max_kb:
                fifo_packets.append(packet)
                fifo_packet_size += packet.size_kb
            else:
                break
        self.buffer = self.buffer[len(fifo_packets):]
        return fifo_packets

class TelemetryRouter:
    def __init__(self, queue: List[TelemetryPacket], max_queue_size: int):
        self.queue = queue
        self.max_queue_size = max_queue_size

    def ingest(self, packets: List[TelemetryPacket]) -> None:
        for packet in packets:
            if len(self.queue) == self.max_queue_size:
                pack_min = min(self.queue)  # This is used because of the __lt__ method so it gives us the element with highest id and highest priority
                self.queue.remove(pack_min)
            self.queue.append(packet)
        return

    def route_next(self) -> Optional[TelemetryPacket]:
        if self.queue:
            hp = min(self.queue)
            self.queue.remove(hp)
            return hp
        return None

    def queue_status(self) -> List[Dict[str, Union[int, float]]]:
        summaries = []
        for item in self.queue:
            data = {
                "satellite_id": item.satellite_id,
                "packet_id": item.packet_id,
                "priority": item.priority,
                "size_kb": item.size_kb,
                "data_size": len(item.data)
            }
            summaries.append(data)
        return summaries

##### NOT NEEDED ANYMORE #####
# Case 2: If the queue is full - drop only the lowest-priority packet.
# Somehow I need to figure out the lowest priority - this is about iterating through the queue
# O(n) to figure out the lowest priority then filter see len of that then remove (this is the inefficient way)
# all_priorities = set()
# for pack in self.queue:
#     all_priorities.add(pack.priority)
# lowest_priority = min(all_priorities)
# # I want to return the lowest priority packets and then look at packet_id
# lowest_p_packets = [packets for packets in self.queue if packets.priority == lowest_priority]
# if not lowest_p_packets:
#     return
# elif len(lowest_p_packets) == 1:
#     return self.queue.remove(lowest_p_packets[0])  # I dislike this but we only have one item to remove
# else:
#     highest_id_packet = lowest_p_packets[0]
#     for p in lowest_p_packets[1:]:
#         if p.packet_id > highest_id_packet.packet_id:
#             highest_id_packet = p
#     return self.queue.remove(highest_id_packet)
# Formally in route_next()
# hp_packet = None
# max_priority = max([pack.priority for pack in self.queue])
# # For item in queue if item.priority == max_priority then compare with item in the highest_priority_packet if None
# # then you become the highest priority packet. Else have logic that compares
# for el in self.queue:
#     if el.priority == max_priority:
#         if not hp_packet:
#             hp_packet = el
#         if el.packet_id > hp_packet.packet_id:
#             hp_packet = el
#         self.queue.remove(hp_packet)
# return hp_packet
