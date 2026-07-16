# ResetOption (System API)

Options for resetting eUICC memory.

**Since:** 18

<!--Device-eSIM-export enum ResetOption--><!--Device-eSIM-export enum ResetOption-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## DELETE_OPERATIONAL_PROFILES

```TypeScript
DELETE_OPERATIONAL_PROFILES = 1
```

Deletes all operational profiles on reset.

**Since:** 18

<!--Device-ResetOption-DELETE_OPERATIONAL_PROFILES = 1--><!--Device-ResetOption-DELETE_OPERATIONAL_PROFILES = 1-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## DELETE_FIELD_LOADED_TEST_PROFILES

```TypeScript
DELETE_FIELD_LOADED_TEST_PROFILES = 1 << 1
```

Deletes all field-loaded testing profiles on reset.

**Since:** 18

<!--Device-ResetOption-DELETE_FIELD_LOADED_TEST_PROFILES = 1 << 1--><!--Device-ResetOption-DELETE_FIELD_LOADED_TEST_PROFILES = 1 << 1-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## RESET_DEFAULT_SMDP_ADDRESS

```TypeScript
RESET_DEFAULT_SMDP_ADDRESS = 1 << 2
```

Resets the default SM-DP+ address on reset.

**Since:** 18

<!--Device-ResetOption-RESET_DEFAULT_SMDP_ADDRESS = 1 << 2--><!--Device-ResetOption-RESET_DEFAULT_SMDP_ADDRESS = 1 << 2-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

