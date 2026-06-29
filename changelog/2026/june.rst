--------------------------------------------------------------------------------
                                      Fix                                       
--------------------------------------------------------------------------------

* iosxe
    * Modified ShowPortSecurityAddress
        * Modified parser regex to allow space and parenthesis in remaining_age field.
    * Modified SnmpGetBulk
        * Updated status handling to set success only after matching SNMP response, MIB, or hex value output.
        * Added empty parser test coverage for unmatched command error output.
    * Modified ShowIpv6Interface
        * Updated regex handling to compile patterns once before line
        * Updated nested output creation to use local dictionaries and
        * Updated joined group address matching so brief-style output with
    * Modified ShowIpv6InterfaceBrief
        * Added parsing for unnumbered interface references in brief output.
        * Added unittest coverage for unassigned rows, link-local and global
    * Modified ShowFlowMonitorCache
        * 'show flow monitor {name} cache'
    * Modified ShowSdmPrefer
        * Made 'vrf_count' field optional in schema to support outputs that do not contain the 'VRF'
    * Modified ShowDeviceTrackingDatabaseMacDetails
        * show device-tracking database mac details Better handling for MACs with no bound IP
    * Modified ShowBgpAllDetail
        * Updated next-hop parsing to support IPv6 next-hop lines with link-local addresses, preventing parser crashes on RFC5549 BGP output.
    * Modified ShowMacAddressTableCount
        * Made 'total_mac_address_space' Optional in schema to support output
    * Modified ShowMacAddressTableCountVlan
        * Made 'Total_mac_address_space' Optional in schema to support output
    * Modified ShowUACUplink, ShowUACUplinkDB, ShowUACActivePort, ShowUACActiveVlan
        * Added rv1 parser support for these commands.
    * Fixed show module parser
        * Relaxed ShowModule schema so blank/empty module slots in stacked
    * Modified ShowPortSecurityAddress
        * Modified ShowPortSecurityAddress parser to handle multiple MACs per interface.
    * Modified ShowOspfv3RibRedistribution
        * Added Optional source_vrf key to schema.
        * Added p_vrf regex pattern to parse source_vrf from route origin
        * Updated p1 regex pattern to support VRF headers in OSPFv3 RIB
    * Modified ShowFlowMonitorCache parser
        * Parser now correctly handles show flow monitor cache states.
    * Modified ShowPlatformSoftwareFedSwitchWdavcFlows parser
        * Added new regex to capture the new output of the command "show platform software fed switch wdavc flows".
    * Modified ShowPlatformsoftwarefedswitchactivesecurityfedpmifid parser
        * Modified the existing regex to capture the new output of the command "show platform software fed switch active security fed pmifid".
    * Modified ShowInventory (rv1)
        * Fixed PID-keyed clobber for multi-chassis SVL pairs (e.g.,
    * Fixed show xfsu eligibility parser
        * Updated schema and parser for xfsu eligibility parser.

* nxos
    * Modified ShowModule
        * Moved LFM modules from LC to XBAR section to avoid CTC LC collection failures

* iosxr
    * Modified ShowIpv6VrfAllInterface
        * Added regex to parse "IPv6 is down (link local duplicate)" state so the 'enabled' key is populated and the schema does not raise a missing key error.
    * Modified AdminShowDiagChassis
        * Changed 'vid' key from required to Optional in the schema so that chassis with an empty/blank "Version Identifier" field in 'admin show diag chassis' output no longer raise a SchemaMissingKeyError.


--------------------------------------------------------------------------------
                                      New                                       
--------------------------------------------------------------------------------

* iosxe
    * Added ShowWrrQueueBandwidth
        * Added schema and parser for 'show wrr-queue bandwidth'
    * Added ShowWrrQueueCosMap
        * Added schema and parser for 'show wrr-queue cos-map'
    * Added ShowIpPortbundleStatus
        * Added schema and parser for 'show ip portbundle status'
    * Added ShowCloudMgmtConfigUpdater
        * Added new parser for 'show cloud-mgmt config-updater' command. This parser is the same as the one for 'show meraki config updater'.
    * Added ShowSubscriberService
        * Added schema and parser for 'show subscriber service'
    * Added ShowFlowRecordName
        * Added schema and parser for 'show flow record {record_name}'
    * Added ShowLispNamedServicesServer for
        * show lisp instance-id {instance_id} named-services server
        * show lisp {lisp_id} instance-id {instance_id} named-services server
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server
    * Added ShowLispNamedServicesServerDetail for
        * show lisp instance-id {instance_id} named-services server detail
        * show lisp instance-id {instance_id} named-services server name {site_name}
        * show lisp instance-id {instance_id} named-services server {eid}
        * show lisp instance-id {instance_id} named-services server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} named-services server detail
        * show lisp {lisp_id} instance-id {instance_id} named-services server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} named-services server {eid}
        * show lisp {lisp_id} instance-id {instance_id} named-services server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server etr-address {etr_address}
    * Added ShowPlatformConditions
        * Added schema and parser for 'show platform conditions'
    * Added ShowRedirectTranslationsIncludeIp
        * Added schema and parser for 'show redirect translations | include <IP>'
    * Added ShowSubscriberSessionDetailed
        * Added schema and parser for 'show subscriber session detailed'
    * Added ShowOspfv3DatabaseExternal
        * show ospfv3 database external
        * show ospfv3 vrf {vrf} database external
    * Added ShowOspfv3DatabaseNssaExternal
        * show ospfv3 database nssa-external
        * show ospfv3 vrf {vrf} database nssa-external
    * Added ShowLispNamedServicesSubscriber
        * For
            * show lisp {lisp_id} instance-id {instance_id} named-services subscriber
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscriber
            * show lisp instance-id {instance_id} named-services subscriber
    * Added ShowLispNamedServicesPublisher
        * For
            * show lisp {lisp_id} instance-id {instance_id} named-services publisher
            * show lisp locator-table {vrf} instance-id {instance_id} named-services publisher
            * show lisp instance-id {instance_id} named-services publisher
    * Added ShowLispNamedServicesSubscription
        * For
            * show lisp {lisp_id} instance-id {instance_id} named-services subscription
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription
            * show lisp instance-id {instance_id} named-services subscription
    * Added ShowLispNamedServicesSubscriptionPrefix
        * For
            * show lisp instance-id {instance_id} named-services subscription {eid_prefix}
            * show lisp {lisp_id} instance-id {instance_id} named-services subscription {eid_prefix}
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription {eid_prefix}
            * show lisp instance-id {instance_id} named-services subscription detail
            * show lisp {lisp_id} instance-id {instance_id} named-services subscription detail
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription detail
    * Added ShowLispNamedServicesServerSubscription
        * For
            * show lisp {lisp_id} instance-id {instance_id} named-services server subscription
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription
            * show lisp instance-id {instance_id} named-services server subscription
    * Added ShowLispNamedServicesServerSubscriptionPrefix
        * For
            * show lisp instance-id {instance_id} named-services server subscription {eid_prefix}
            * show lisp {lisp_id} instance-id {instance_id} named-services server subscription {eid_prefix}
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription {eid_prefix}
            * show lisp instance-id {instance_id} named-services server subscription detail
            * show lisp {lisp_id} instance-id {instance_id} named-services server subscription detail
            * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription detail
    * Added ShowPlatformHardwareFedSwitchForwardLastSummary
        * Added schema and parser for 'show platform hardware fed {switch} {mode} forward last summary'
    * Added ShowVpdnTunnelAll
        * Added schema and parser for 'show vpdn tunnel all'
    * Added ShowIpIgmpSnooping
        * Added schema and parser for 'show ip igmp snooping'
    * Added ShowCloudMgmtConfigUpdater
        * Added new parser for 'show cloud-mgmt config-updater' command. This parser is the same as the one for 'show meraki config updater'.
    * Added ShowPlatformHardwareQfpActiveFeatureL2bdDatapathSystem
        * Added schema and parser for 'show platform hardware qfp active feature l2bd datapath system'
    * Added ShowRomvar (rv1)
        * Added role aware ROMMON variable output for HA devices.
    * Modified ShowRomvar
        * Tightened numeric ROMMON field parsing for NO_CONSOLE, BOARDID,
        * Added DEBUG_CONF key
    * Added ShowSubscriberSessionDetail
        * Added schema and parser for 'show subscriber session detail'
    * Modified ShowOspfv3RibRedistribution
        * show ospfv3 vrf {vrf} rib redistribution
    * Added ShowOtvSummary
        * Added schema and parser for 'show otv summary'
    * Added ShowOtvIsisNeighbors
        * Added schema and parser for 'show otv isis neighbors'
    * Added ShowOtvRoute
        * Added schema and parser for 'show otv route'
    * Added ShowIdmgrSessionKeyId
        * Added schema and parser for 'show idmgr session key aaa-unique-id {aaa_unique_id}'
    * Added ShowLispMultihomingSiteId
        * show lisp multihoming site-id *
        * show lisp multihoming site-id {site_id}
    * Added ShowLispMultihomingSiteIdDetail
        * show lisp multihoming site-id * detail
        * show lisp multihoming site-id {site_id} detail
    * Added ShowVlansDot1qVlanIdGigabitethernet300Interface
        * Added schema and parser for 'show vlans dot1q {vlan_id} gigabitethernet3/0/0 {interface}'
    * Added ShowVpdnGroupSelectSummary
        * Added schema and parser for 'show vpdn group-select summary'
    * Added ShowSubscriberSessionAll
        * Added schema and parser for 'show subscriber session all'
    * Added ShowPlatformSoftwareInfrastructureThreadFastpath
        * Added schema and parser for 'show platform software infrastructure thread fastpath'
    * Added ShowVpdnSessionAll
        * show vpdn session all
    * Added ShowPolicyMapSessionOut
        * Added schema and parser for 'show policy-map session out'
    * Added ShowPlatformSoftwareEssFpActiveL4r
        * Added schema and parser for 'show platform software ess fp active l4r'
    * Added ShowPlatformHardwareQfpActiveInterfaceIfNameStatistics
        * Added schema and parser for 'show platform hardware qfp active interface if-name {interface} statistics'
    * Added ShowPlatformHardwareQfpActiveInterfaceIfNamePath
        * Added schema and parser for 'show platform hardware qfp active interface if-name {interface} path'

* nxos
    * Added ShowIpPimHostProxy
        * show ip pim host-proxy


--------------------------------------------------------------------------------
                                  Processing.                                   
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
                                    Modified                                    
--------------------------------------------------------------------------------

* iosxe
    * Updated ShowLispSiteSuperParser regexes (p2, p3_2) to accept DN-string EID prefixes (e.g. ``firewall``, ``dual-stack``) used by named-services output.
    * Updated ShowLispSiteDetailSuperParser regex (p3) to accept DN-string EID prefixes in ``EID-prefix <name> instance-id <id>`` lines for named-services server detail output.
    * Modified ShowLispSubscriptionSuperParser
        * Updated eid_prefix regex to accept distinguished-name style EID prefixes
    * Modified ShowLispSubscriptionPrefixSuperParser
        * Updated eid_prefix regex to accept distinguished-name style EID prefixes
    * Modified ShowLispServerSubscriptionSuperParser
        * Updated eid_prefix and registration regex to accept distinguished-name style EID prefixes
    * Modified ShowLispServerSubscriptionPrefixSuperParser
        * Updated eid_prefix regex to accept distinguished-name style EID prefixes
    * Added ShowLispNamedServicesPublication
        * show lisp instance-id {instance_id} named-services publication
        * show lisp {lisp_id} instance-id {instance_id} named-services publication
        * show lisp locator-table {vrf} instance-id {instance_id} named-services publication
    * Added ShowLispNamedServicesPublicationPrefix
        * show lisp instance-id {instance_id} named-services publication {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} named-services publication {eid_prefix}
        * show lisp locator-table {vrf} instance-id {instance_id} named-services publication {eid_prefix}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} named-services publication {eid_prefix}


--------------------------------------------------------------------------------
                                    Strings.                                    
--------------------------------------------------------------------------------


