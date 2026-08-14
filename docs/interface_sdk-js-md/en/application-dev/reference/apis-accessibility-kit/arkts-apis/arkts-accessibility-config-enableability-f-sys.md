# enableAbility (System API)

## Modules to Import

```TypeScript
import { config } from 'config';
```

## enableAbility

```TypeScript
function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>
```

Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)). This API uses a promise to return the result. Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>--><!--Device-config-function enableAbility(name: string, capability: Array<accessibility.Capability>): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the accessibility extension app, in the format of 'bundleName/abilityName'. |
| capability | Array&lt;accessibility.Capability&gt; | Yes | Capability attributes of the accessibility extension app. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) | Invalid bundle name or ability name. |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) | Target ability already enabled. |


## enableAbility

```TypeScript
function enableAbility(
    name: string,
    capability: Array<accessibility.Capability>,
    callback: AsyncCallback<void>
  ): void
```

Enables an accessibility extension. This API must be used together with [config.disableAbility](arkts-accessibility-config-disableability-f-sys.md#disableAbility-(System-API)). This API uses an asynchronous callback to return the result. Compared with [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)), this API only enables the accessibility extension without listening for connection state changes. To listen for disconnection events of the accessibility extension, use [config.enableAbilityWithCallback](arkts-accessibility-config-enableabilitywithcallback-f-sys.md#enableAbilityWithCallback-(System-API)).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function enableAbility(    name: string,    capability: Array<accessibility.Capability>,    callback: AsyncCallback<void>  ): void--><!--Device-config-function enableAbility(    name: string,    capability: Array<accessibility.Capability>,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the accessibility extension app, in the format of 'bundleName/abilityName'. |
| capability | Array&lt;accessibility.Capability&gt; | Yes | Capability attribute of the accessibility extension app. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the accessibility extension is enabled successfully, **err** is undefined; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) | Invalid bundle name or ability name. |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) | Target ability already enabled. |

