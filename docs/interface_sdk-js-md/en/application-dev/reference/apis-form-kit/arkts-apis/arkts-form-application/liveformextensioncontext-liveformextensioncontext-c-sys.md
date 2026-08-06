# LiveFormExtensionContext

LiveFormExtensionContext**, inherited from  
[ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, is the context of  
[LiveFormExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Inheritance/Implementation:** LiveFormExtensionContext extends [ExtensionContext](../../../apis-ability-kit/arkts-apis/arkts-ability-application/extensioncontext-extensioncontext-c.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## connectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long
```

Connect a service extension ability.The destination of the connection must be a service extension.You must implement the \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ interface to obtain the proxy of the target service extension when the Service extension is connected.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long--><!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the service extension to connect. |
| connection | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the callback of connection. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Returns the connection id. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [16500100](../../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |
| [16501000](../../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16501011](../../errorcode-form.md#16501011-api-not-supported) | The form can not support this operation |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
public disconnectServiceExtensionAbility(connectionId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
public disconnectServiceExtensionAbility(connectionId: long): Promise<void>
```

Disconnect an ability to a service extension, in contrast to \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>--><!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connectionId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Yes | the connection id returned from connectServiceExtensionAbility api. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |
| [16501000](../../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16501011](../../errorcode-form.md#16501011-api-not-supported) | The form can not support this operation |

