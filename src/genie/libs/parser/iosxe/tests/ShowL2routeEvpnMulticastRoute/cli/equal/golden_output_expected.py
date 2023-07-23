
expected_output = {
    'evi' : {
        '100': {
            'etag' : {
                '100': {
                    'group' : {
                        '224.1.1.1': {
                            'source' : {
                                '*': {
                                    'etag': '100',
                                    'evi': '100',
                                    'group': '224.1.1.1',
                                    'nexthops': 'V:101 227.1.1.1, '
                                    'Et0/3:100, Et0/3:200, '
                                    'Et0/1:100, Et0/1:200',
                                    'source': '*'
                                    },
                                '172.1.1.1': {
                                    'etag': '100',
                                    'evi': '100',
                                    'group': '224.1.1.1',
                                    'nexthops': 'V:101 '
                                    '227.1.1.1, '
                                    'Et0/2:100, '
                                    'Et0/3:200, '
                                    'Et0/1:100, '
                                    'Et0/1:200',
                                    'source': '172.1.1.1'
                                },
                                '172.1.1.2': {
                                    'etag': '100',
                                    'evi': '100',
                                    'group': '224.1.1.1',
                                    'nexthops': 'V:101 '
                                    '227.1.1.1, '
                                    'Et0/2:100, '
                                    'Et0/3:100, '
                                    'Et0/1:100, '
                                    'Et0/1:200',
                                    'source': '172.1.1.2'
                                },
                                '172.1.1.3': {
                                    'etag': '100',
                                    'evi': '100',
                                    'group': '224.1.1.1',
                                    'nexthops': 'Et0/2:300, '
                                    'V:101 '
                                    '227.1.1.1, '
                                    'Et0/3:100, '
                                    'Et0/3:200, '
                                    'Et0/1:100, (& '
                                    'more)',
                                    'source': '172.1.1.3'
                                },
                                '172.1.1.4': {
                                    'etag': '100',
                                    'evi': '100',
                                    'group': '224.1.1.1',
                                    'nexthops': 'Et0/2:300, '
                                    'V:101 '
                                    '227.1.1.1, '
                                    'Et0/3:100, '
                                    'Et0/3:200, '
                                    'Et0/1:100, (& '
                                    'more)',
                                    'source': '172.1.1.4'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
