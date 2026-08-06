# CdsmClient

Manages a CDSM client instance. Before invoking any CDSM client method,you must use \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to create a CDSM client instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cdsm-interface CdsmClient--><!--Device-cdsm-interface CdsmClient-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## getCdsmInfo

```TypeScript
getCdsmInfo(): CdsmInfo
```

Gets the coordinated devices set information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-getCdsmInfo(): CdsmInfo--><!--Device-CdsmClient-getCdsmInfo(): CdsmInfo-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the coordinated devices set information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |

## offCdsmInfoChange

```TypeScript
offCdsmInfoChange(callback?: Callback<CdsmInfo>): void
```

Unsubscribes from coordinated devices set information change event.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-offCdsmInfoChange(callback?: Callback<CdsmInfo>): void--><!--Device-CdsmClient-offCdsmInfoChange(callback?: Callback<CdsmInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CdsmInfo&gt; | No | Callback used to listen for the coordinated devices set information. |

## onCdsmInfoChange

```TypeScript
onCdsmInfoChange(callback: Callback<CdsmInfo>): void
```

Subscribes to coordinated devices set information change event.

This event is accessible only to applications that granted the ohos.permission.NEARLINK\_ACCESS permission.If the application is granted the ohos.permission.GET\_NEARLINK\_PEER\_MAC permission,the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmClient-onCdsmInfoChange(callback: Callback<CdsmInfo>): void--><!--Device-CdsmClient-onCdsmInfoChange(callback: Callback<CdsmInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CdsmInfo&gt; | Yes | Callback used to listen for the coordinated devices set information. |

