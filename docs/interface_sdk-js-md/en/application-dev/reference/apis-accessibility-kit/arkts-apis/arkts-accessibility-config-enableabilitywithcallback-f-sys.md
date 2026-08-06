# enableAbilityWithCallback (System API)

## enableAbilityWithCallback

```TypeScript
function enableAbilityWithCallback(
    name: string,
    capability: Array<accessibility.Capability>,
    connectCallback: ConnectCallback
  ): Promise<void>
```

Enables the auxiliary extension ability and specifies [ConnectCallback]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to be invoked when the state of an auxiliary extension ability changes. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-config-function enableAbilityWithCallback(    name: string,    capability: Array<accessibility.Capability>,    connectCallback: ConnectCallback  ): Promise<void>--><!--Device-config-function enableAbilityWithCallback(    name: string,    capability: Array<accessibility.Capability>,    connectCallback: ConnectCallback  ): Promise<void>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the accessibility extension ability, in the format of 'bundleName/abilityName'. |
| capability | Array&lt;accessibility.Capability&gt; | Yes | Capabilities of the auxiliary extension ability. |
| connectCallback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback to be invoked when the state of an auxiliary extension ability changes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [9300001](../errorcode-accessibility.md#9300001-invalid-bundle-name-or-ability-name) | Invalid bundle name or ability name. |
| [9300002](../errorcode-accessibility.md#9300002-target-ability-already-enabled) | Target ability already enabled. |

