expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_table': 'vrf red ',
                    'entries': 1,
                    'eid_prefix': {
                        '20.20.1.100/32': {
                            'uptime': '00:00:00',
                            'expiry_time': '00:01:08',
                            'via': 'map-reply',
                            'map_reply_state': 'unknown-eid-forward',
                            'site': 'remote-to-site',
                            'sgt': 10,
                            'map_cache_type': 'software only',
                            'locators': {
                                '10.0.1.2': {
                                    'uptime': '00:00:00',
                                    'rloc_state': 'up',
                                    'priority': 0,
                                    'weight': 0,
                                    'encap_iid': '-'
                                    },
                                '10.0.1.5': {
                                    'uptime': '00:00:00',
                                    'rloc_state': 'admin-down',
                                    'priority': 255,
                                    'weight': 0,
                                    'encap_iid': '-'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }