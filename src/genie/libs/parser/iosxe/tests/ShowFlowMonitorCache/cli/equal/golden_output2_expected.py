expected_output = {
    'cache_size': 10000,
    'cache_type': 'Normal (Platform cache)',
    'current_entries': 1,
    'entries': {
        0: {
            'counter_bytes': 354176,
            'counter_pkts_long': 2767,
            'datalink_vlan_input': '15',
            'flow_direction': 'Input',
            'ip_protocol': 6,
            'ipv4_dst_addr': '172.51.15.111',
            'ipv4_dst_mask': '/0',
            'ipv4_nxt_hop': '0.0.0.0',
            'ipv4_src_addr': '172.51.15.11',
            'ipv4_src_mask': '/0',
            'tcp_flags': '0x00',
            'timestamp_abs_first': '10:32:05.886',
            'timestamp_abs_last': '10:35:15.886',
            'trns_dst_port': 100,
            'trns_src_port': 1,
            'vxlan_vni_id': '20015',
            'vxlan_vtep_input': '172.11.1.2',
            'vxlan_vtep_output': '172.11.1.1',
        },
    },
    'flows_added': 3302,
    'flows_aged': {
        'active_timeout': 2475,
        'active_timeout_secs': 180,
        'inactive_timeout': 826,
        'inactive_timeout_secs': 60,
        'total': 3301,
    },
}