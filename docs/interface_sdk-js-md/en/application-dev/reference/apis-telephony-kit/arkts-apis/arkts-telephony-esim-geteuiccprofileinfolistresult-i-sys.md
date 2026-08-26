# GetEuiccProfileInfoListResult (System API)

Obtains the profile information list.

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## isRemovable

```TypeScript
isRemovable: boolean
```

Whether the eUICC is removable. The value **true** indicates that the eUICC is removable, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## profiles

```TypeScript
profiles: Array<EuiccProfile>
```

Profile array.

**Type:** Array&lt;[EuiccProfile](arkts-telephony-esim-euiccprofile-i-sys.md)&gt;

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

## responseResult

```TypeScript
responseResult: ResultCode
```

Promise used to return the operation result.

**Type:** ResultCode

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.
