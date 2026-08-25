# enableAbility (System API)

## Modules to Import

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## enableAbility

```TypeScript
function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>
```

Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md). This API uses a promise to return the result.Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md).

**Since:** 9

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| capability | Array & lt;accessibility.Capability & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) |


## enableAbility

```TypeScript
function enableAbility(
    name: string,
    capability: Array<accessibility.Capability>,
    callback: AsyncCallback<void>
  ): void
```

Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md). This API uses an asynchronous callback to return the result.Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md).

**Since:** 9

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| capability | Array & lt;accessibility.Capability & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) |
