expected_output = {
    "beacon_led_status": "off",
    "fantray_details": {
        1: {
            "fan": {"Fan1": 3180, "Fan2": 3240, "Fan3": 3120, "Fan4": 3120},
            "interrupt_source": "0x0",
            "press": 100,
            "temp": 24,
            "throttle": "35%",
        },
        2: {
            "fan": {"Fan1": 3000, "Fan2": 3180, "Fan3": 3060, "Fan4": 3120},
            "interrupt_source": "0x0",
            "press": 100,
            "temp": 24,
            "throttle": "35%",
        },
        3: {
            "fan": {"Fan1": 3150, "Fan2": 3150, "Fan3": 3210, "Fan4": 3120},
            "interrupt_source": "0x0",
            "press": 100,
            "temp": 24,
            "throttle": "35%",
        },
        4: {
            "fan": {"Fan1": "N/A", "Fan2": "N/A", "Fan3": "N/A", "Fan4": "N/A"},
            "interrupt_source": "N/A",
            "press": "N/A",
            "temp": "N/A",
            "throttle": "N/A",
        },
    },
    "global_version": 17050302,
    "interrupt_source_register": 34560,
    "status_led": "green",
}