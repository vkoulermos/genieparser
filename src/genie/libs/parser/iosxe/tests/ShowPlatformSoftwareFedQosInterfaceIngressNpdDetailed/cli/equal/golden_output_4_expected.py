expected_output = {
    'bind_information': {
        'iqp_counter_oid': '0x0',
        'iqp_counter_size': 1,
        'meter_set_info': {
            '0': {
                'action_profile_oid': '0x110',
                'cir': 1000000000,
                'eir': 1000000000,
                'profile_oid': '0x86D',
            },
            '1': {
                'action_profile_oid': '0x110',
                'cir': 500000000,
                'eir': 500000000,
                'profile_oid': '0x877',
            },
            '2': {
                'action_profile_oid': '0x0',
                'cir': 0,
                'eir': 0,
                'profile_oid': '0x0',
            },
        },
        'meter_set_oid': '0x85B',
        'meter_type': 'IFG EXACT',
        'no_of_meters': 3,
        'port_internal_state': 'Active',
        'port_oid': '0x0',
        'port_type': 'L2 ETHER CHANNEL',
        'speed': 40000000000,
        'system_port_oid': '0x0',
    },
    'interface': {
        'Port-channel10': {
            'cgid': '0x738310',
            'filter_state': 'UP TO DATE',
            'no_of_classes': 3,
            'tcg_ref_count': 1,
            'vmr_state': 'UP TO DATE',
        },
    },
    'ipv4_acl': {
        'number_of_aces': 0,
        'oid': '0x0',
    },
    'ipv6_acl': {
        'number_of_aces': 0,
        'oid': '0x0',
    },
    'qos_profile_information': {
        'cos_dei': {
            '0': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 0,
                'tc': 0,
            },
            '1': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 1,
                'tc': 0,
            },
            '10': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 1,
                'meter': 'Y',
                'qos_group': 0,
                'remap': 10,
                'tc': 7,
            },
            '11': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 1,
                'meter': 'Y',
                'qos_group': 0,
                'remap': 11,
                'tc': 7,
            },
            '12': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 12,
                'tc': 0,
            },
            '13': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 13,
                'tc': 0,
            },
            '14': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 14,
                'tc': 0,
            },
            '15': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 15,
                'tc': 0,
            },
            '2': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 0,
                'meter': 'Y',
                'qos_group': 0,
                'remap': 2,
                'tc': 0,
            },
            '3': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 0,
                'meter': 'Y',
                'qos_group': 0,
                'remap': 3,
                'tc': 0,
            },
            '4': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 4,
                'tc': 0,
            },
            '5': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 5,
                'tc': 0,
            },
            '6': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 6,
                'tc': 0,
            },
            '7': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 7,
                'tc': 0,
            },
            '8': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 8,
                'tc': 7,
            },
            '9': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 9,
                'tc': 7,
            },
        },
        'dscp': {
            '0': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 0,
                'tc': 0,
            },
            '1': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 1,
                'tc': 0,
            },
            '10': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 10,
                'tc': 0,
            },
            '11': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 11,
                'tc': 0,
            },
            '12': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 12,
                'tc': 0,
            },
            '13': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 13,
                'tc': 0,
            },
            '14': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 14,
                'tc': 0,
            },
            '15': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 15,
                'tc': 0,
            },
            '16': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 16,
                'tc': 7,
            },
            '17': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 17,
                'tc': 0,
            },
            '18': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 18,
                'tc': 0,
            },
            '19': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 19,
                'tc': 0,
            },
            '2': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 2,
                'tc': 0,
            },
            '20': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 20,
                'tc': 0,
            },
            '21': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 21,
                'tc': 0,
            },
            '22': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 22,
                'tc': 0,
            },
            '23': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 23,
                'tc': 0,
            },
            '24': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 24,
                'tc': 7,
            },
            '25': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 25,
                'tc': 0,
            },
            '26': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 26,
                'tc': 0,
            },
            '27': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 27,
                'tc': 0,
            },
            '28': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 28,
                'tc': 0,
            },
            '29': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 29,
                'tc': 0,
            },
            '3': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 3,
                'tc': 0,
            },
            '30': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 30,
                'tc': 0,
            },
            '31': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 31,
                'tc': 0,
            },
            '32': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 32,
                'tc': 7,
            },
            '33': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 33,
                'tc': 0,
            },
            '34': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 34,
                'tc': 0,
            },
            '35': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 35,
                'tc': 0,
            },
            '36': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 36,
                'tc': 0,
            },
            '37': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 37,
                'tc': 0,
            },
            '38': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 38,
                'tc': 0,
            },
            '39': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 39,
                'tc': 0,
            },
            '4': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 4,
                'tc': 0,
            },
            '40': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 40,
                'tc': 7,
            },
            '41': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 41,
                'tc': 0,
            },
            '42': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 42,
                'tc': 0,
            },
            '43': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 43,
                'tc': 0,
            },
            '44': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 44,
                'tc': 0,
            },
            '45': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 45,
                'tc': 0,
            },
            '46': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 46,
                'tc': 7,
            },
            '47': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 47,
                'tc': 0,
            },
            '48': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 48,
                'tc': 7,
            },
            '49': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 49,
                'tc': 0,
            },
            '5': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 5,
                'tc': 0,
            },
            '50': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 50,
                'tc': 0,
            },
            '51': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 51,
                'tc': 0,
            },
            '52': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 52,
                'tc': 0,
            },
            '53': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 53,
                'tc': 0,
            },
            '54': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 54,
                'tc': 0,
            },
            '55': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 55,
                'tc': 0,
            },
            '56': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 56,
                'tc': 7,
            },
            '57': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 57,
                'tc': 0,
            },
            '58': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 58,
                'tc': 0,
            },
            '59': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 59,
                'tc': 0,
            },
            '6': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 6,
                'tc': 0,
            },
            '60': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 60,
                'tc': 0,
            },
            '61': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 61,
                'tc': 0,
            },
            '62': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 62,
                'tc': 0,
            },
            '63': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 63,
                'tc': 0,
            },
            '7': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 7,
                'tc': 0,
            },
            '8': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 8,
                'tc': 0,
            },
            '9': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 9,
                'tc': 0,
            },
        },
        'exp': {
            '0': {
                'dp': 'G',
                'encap': 0,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 0,
                'tc': 0,
            },
            '1': {
                'dp': 'G',
                'encap': 1,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 1,
                'tc': 0,
            },
            '2': {
                'dp': 'G',
                'encap': 2,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 2,
                'tc': 0,
            },
            '3': {
                'dp': 'G',
                'encap': 3,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 3,
                'tc': 0,
            },
            '4': {
                'dp': 'G',
                'encap': 4,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 4,
                'tc': 0,
            },
            '5': {
                'dp': 'G',
                'encap': 5,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 5,
                'tc': 0,
            },
            '6': {
                'dp': 'G',
                'encap': 6,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 6,
                'tc': 0,
            },
            '7': {
                'dp': 'G',
                'encap': 7,
                'mc_offset': 2,
                'meter': 'N',
                'qos_group': 0,
                'remap': 7,
                'tc': 0,
            },
        },
        'need_filter_table_update': 'UPTODATE',
        'no_of_counter': 1,
        'no_of_meters': 2,
        'oid': '0x840',
        'ref_count': 1,
        'tunnel_mode': 'RE-EVALUATE',
    },
}