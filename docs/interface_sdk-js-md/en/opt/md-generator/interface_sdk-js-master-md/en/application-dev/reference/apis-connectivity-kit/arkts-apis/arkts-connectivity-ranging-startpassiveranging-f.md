# startPassiveRanging

## Modules to Import

```TypeScript
```

## startPassiveRanging

```TypeScript
function startPassiveRanging(capabilityType: RangingTypes): Promise<number>
```

Starts passive ranging mode. Upon successful startup, returns a handle identifier for the passive ranging session and begins broadcasting ranging packets. The returned handle can be used to stop the passive ranging broadcast via stopPassiveRanging.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ranging-function startPassiveRanging(capabilityType: RangingTypes): Promise<int>--><!--Device-ranging-function startPassiveRanging(capabilityType: RangingTypes): Promise<int>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [capabilityType](arkts-connectivity-ranging-rangingparams-i.md) | [RangingTypes](arkts-connectivity-ranging-rangingtypes-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 34900052 |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 34900053 |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
