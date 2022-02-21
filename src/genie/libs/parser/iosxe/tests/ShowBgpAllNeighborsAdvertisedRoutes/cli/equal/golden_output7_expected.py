expected_output = {
    "vrf": {
        "default": {
            "neighbor": {
                "10.106.101.1": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "advertised": {},
                            "bgp_table_version": 5482065,
                            "local_router_id": "10.250.102.43",
                        },
                        "vpnv4 unicast RD 35432:20": {
                            "bgp_table_version": 5482065,
                            "local_router_id": "10.250.102.43",
                            "route_distinguisher": "35432:20",
                            "default_vrf": "MOBILE_GRX",
                            "advertised": {
                                "0.0.0.0": {
                                    "index": {
                                        1: {
                                            "localprf": 120,
                                            "metric": 100,
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "path": "(64615 64630 64602 64628 64605) 6762",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "1.20.122.0/27": {
                                    "index": {
                                        1: {
                                            "localprf": 120,
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 35030 56120 72001",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "202.179.206.0": {
                                    "index": {
                                        1: {
                                            "localprf": 120,
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 6774 64666 64666 64666",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                },
                                "202.191.98.144/29": {
                                    "index": {
                                        1: {
                                            "localprf": 120,
                                            "next_hop": "192.168.12.168",
                                            "origin_codes": "i",
                                            "path": "(64615 64628 64603 64629 64601 64630 64609) 6762 58453 136255",
                                            "status_codes": "*>",
                                            "weight": 0,
                                        }
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}
