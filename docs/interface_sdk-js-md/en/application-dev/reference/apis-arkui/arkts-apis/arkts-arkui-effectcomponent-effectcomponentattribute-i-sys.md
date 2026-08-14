# EffectComponentAttribute (System API)

Define the EffectComponentAttribute.

**Inheritance/Implementation:** EffectComponentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface EffectComponentAttribute--><!--Device-unnamed-export declare interface EffectComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## alwaysSnapshot

```TypeScript
alwaysSnapshot(enable: boolean | undefined): this
```

Use snapshot when Effect Component have no visual effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentAttribute-alwaysSnapshot(enable: boolean | undefined): this--><!--Device-EffectComponentAttribute-alwaysSnapshot(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | <br>true indicates using the snapshot method, false indicates not using the snapshot method. undefined means the default value false. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A nonsystem application calls a system API. |

## default

```TypeScript
default
```

Set EffectComponent options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentAttribute-default--><!--Device-EffectComponentAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

