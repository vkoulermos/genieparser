expected_output = {
    "vrf": {
        "default": {
        "neighbor": {
            "10.4.6.6": {
                "address_family": {
                    "vpnv4 unicast": {
                        "bgp_table_version": 5493523,
                        "local_router_id": "10.169.197.25",
                        "routes": {}
                    },
                "vpnv4 unicast RD 35432:20": {
                    "bgp_table_version": 5493523,
                    "default_vrf": "MOBILE_GRX",
                    "local_router_id": "10.169.197.25",
                    "route_distinguisher": "35432:20",
                    "routes": {
                        "0.0.0.0": {
                            "index": {
                                1: {
                                    "localprf": 120,
                                    "metric": 100,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "i",
                                    "path": "(64615 64630 64602 64628 64605) 6762",
                                    "status_codes": "*>",
                                    "weight": 0
                                }
                            }
                        },
                        "1.20.122.0/27": {
                            "index": {
                                1: {
                                    "localprf": 120,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "i",
                                    "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 35030 56120 72001",
                                    "status_codes": "*>",
                                    "weight": 0
                                }
                            }
                        },
                        "27.109.115.224/27": {
                            "index": {
                                1: {
                                    "localprf": 120,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "?",
                                    "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 58453 45498",
                                    "status_codes": "*>",
                                    "weight": 0
                                }
                            }
                        },
                        "221.132.224.0/19": {
                            "index": {
                                1: {
                                    "localprf": 120,
                                    "next_hop": "10.4.6.6",
                                    "origin_codes": "i",
                                    "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 6774 7713 64689",
                                    "status_codes": "*>",
                                    "weight": 0
                                }
                            }
                        }
                    }
                }
            }
            }
        }
        }
    }
}