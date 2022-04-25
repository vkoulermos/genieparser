

expected_output = {
    'vpn_id':{
        1:{
            'ethernet_segment_id':{
                '0012.1212.1212.1212.1212':{
                    'es_index':{
                        1:{
                            'encap':'SRv6',
                            'ether_tag':'0',
                            'internal_id':'None',
                            'mp_resolved':'FALSE',
                            'mp_info':'Remote single-active',
                            'reason':'No valid MAC paths',
                            'mp_iid':'None',
                            'pathlists':{
                                'ead_es':{
                                    'nexthop':{
                                        '2.2.2.2':{
                                            'df_role':'B'
                                        }
                                    }
                                },
                                'ead_evi':{
                                    'nexthop':{
                                        '2.2.2.2':{
                                            'sid':'cafe:0:200:e000::'
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                '0034.3434.3434.3434.3434':{
                    'es_index':{
                        1:{
                            'encap':'SRv6',
                            'ether_tag':'0',
                            'internal_id':'::ffff:10.0.0.71',
                            'mp_resolved':'TRUE',
                            'mp_info':'Remote single-active',
                            'mp_iid':'::ffff:10.0.0.71',
                            'pathlists':{
                                'mac':{
                                    'nexthop':{
                                        '3.3.3.3':{
                                            'sid':'cafe:0:300:e000::'
                                        }
                                    }
                                },
                                'ead_es':{
                                    'nexthop':{
                                        '3.3.3.3':{
                                            'df_role':'P'
                                        },
                                        '4.4.4.4':{
                                            'df_role':'B'
                                        }
                                    }
                                },
                                'ead_evi':{
                                    'nexthop':{
                                        '3.3.3.3':{
                                            'sid':'cafe:0:300:e000::'
                                        },
                                        '4.4.4.4':{
                                            'sid':'cafe:0:400:e000::'
                                        }
                                    }
                                },
                                'summary':{
                                    'nexthop':{
                                        '3.3.3.3':{
                                            'tep_id':'0x05000003',
                                            'df_role':'P',
                                            'sid':'cafe:0:300:e000::'
                                        },
                                        '4.4.4.4':{
                                            'tep_id':'0x00000000',
                                            'df_role':'B',
                                            'sid':'cafe:0:400:e000::'
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