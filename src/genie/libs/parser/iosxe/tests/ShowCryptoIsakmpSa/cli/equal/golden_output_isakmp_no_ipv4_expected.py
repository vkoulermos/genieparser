expected_output = {
        'isakmp_stats': {
            'IPv6':{
                1:{
                    'destination': '100.0.10::2',
                    'source': '100.13.220::2',
                    'session_state': 'QM_IDLE',
                    'conn_id': 29610,
                    'status': 'ACTIVE'
                },
                2:{
                    'destination': '100.0.10::2',
                    'source': '100.12.82::2',
                    'session_state': 'MM_NO_STATE',
                    'conn_id': 29189,
                    'status': 'ACTIVE',
                    'current_status': 'deleted'
                },
                3:{
                    'destination': '100.0.10::2',
                    'source': '100.11.106::2',
                    'session_state': 'QM_IDLE',
                    'conn_id': 29363,
                    'status': 'ACTIVE'
                },
            },
        },
    }