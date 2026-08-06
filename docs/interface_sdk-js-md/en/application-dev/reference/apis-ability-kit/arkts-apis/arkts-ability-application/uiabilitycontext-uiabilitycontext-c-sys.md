# UIAbilityContext

UIAbilityContext provides the context environment for a [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ that needs to store its status. It inherits from [Context]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and provides UIAbility-related configuration and APIs for operating UIAbility and ServiceExtensionAbility components. For example, you can use the APIs to start a UIAbility, terminate a UIAbility to which the UIAbilityContext belongs, and start, terminate, connect to, or disconnect from a ServiceExtensionAbility.

**Inheritance/Implementation:** UIAbilityContext extends [Context](../arkts-ability-context-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIAbilityContext extends Context--><!--Device-unnamed-declare class UIAbilityContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectAbilityWithAccount

```TypeScript
connectAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long
```

Connects this UIAbility to a ServiceExtensionAbility, with the account ID specified. This API can be called only on the main thread.This API can be properly called on phones and tablets. If it is called on other devices, error code 16000006 is returned.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [UIAbilityContext#connectServiceExtensionAbilityWithAccount](uiabilitycontext-uiabilitycontext-c-sys.md#connectserviceextensionabilitywithaccount)(want:

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-connectAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long--><!--Device-UIAbilityContext-connectAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Instance of the callback function after the connection to the ServiceExtensionAbility is set up. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Result code of the connection. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## connectServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbilityWithAccount(want: Want, accountId: number, options: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long
```

Connects this UIAbility to a ServiceExtensionAbility, with the account ID specified. This API can be called only on the main thread.This API can be properly called on phones and tablets. If it is called on other devices, error code 16000006 is returned.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long--><!--Device-UIAbilityContext-connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Instance of the callback function after the connection to the ServiceExtensionAbility is set up. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：long | Result code of the connection. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## disconnectAbility

```TypeScript
disconnectAbility(connection: long, callback: AsyncCallback<void>): void
```

Disconnects from a \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null.This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [UIAbilityContext#disconnectServiceExtensionAbility](uiabilitycontext-uiabilitycontext-c.md#disconnectserviceextensionability)(connection:

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-disconnectAbility(connection: long, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-disconnectAbility(connection: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | long | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by [connectServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Connect to system service failed. 2.System service failed to communicate with dependency module. |

## disconnectAbility

```TypeScript
disconnectAbility(connection: long): Promise<void>
```

Disconnects from a \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null.This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** [UIAbilityContext#disconnectServiceExtensionAbility](uiabilitycontext-uiabilitycontext-c.md#disconnectserviceextensionability)(connection:

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-disconnectAbility(connection: long): Promise<void>--><!--Device-UIAbilityContext-disconnectAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | long | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by [connectServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1. Connect to system service failed. 2.System service failed to communicate with dependency module. |

## requestModalUIExtension

```TypeScript
requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void
```

Requests the specified foreground application to start the UIExtensionAbility of the corresponding type. This API uses an asynchronous callback to return the result. It can be called only on the main thread.The foreground application is specified by **bundleName** in **want.parameters**. If **bundleName** is left unspecified, or if the application specified by **bundleName** is not running in the foreground or does not exist,the UIExtensionAbility is directly started on the system UI. The UIExtensionAbility to start is determined by the combination of the **bundleName**, **abilityName**, and **moduleName** fields in **want**, and its type is determined by the **ability.want.params.uiExtensionType** field in **want.parameters**.Before starting the UIExtensionAbility, ensure that the foreground application has finished page initialization.Otherwise, the UIExtensionAbility fails to start and the error message "uiContent is nullptr" is displayed. The application can determine the time to start the UIExtensionAbility by listening for the page loading status. After the page initialization is successful, the key log information "UIContentImpl: focus again" is recorded.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information used to start the UIExtensionAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |

## requestModalUIExtension

```TypeScript
requestModalUIExtension(pickerWant: Want): Promise<void>
```

Requests the specified foreground application to start the UIExtensionAbility of the corresponding type. This API uses a promise to return the result. It can be called only on the main thread.The foreground application is specified by **bundleName** in **want.parameters**. If **bundleName** is left unspecified, or if the application specified by **bundleName** is not running in the foreground or does not exist,the UIExtensionAbility is directly started on the system UI. The UIExtensionAbility to start is determined by the combination of the **bundleName**, **abilityName**, and **moduleName** fields in **want**, and its type is determined by the **ability.want.params.uiExtensionType** field in **want.parameters**.Before starting the UIExtensionAbility, ensure that the foreground application has finished page initialization.Otherwise, the UIExtensionAbility fails to start and the error message "uiContent is nullptr" is displayed. The application can determine the time to start the UIExtensionAbility by listening for the page loading status. After the page initialization is successful, the key log information "UIContentImpl: focus again" is recorded.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want): Promise<void>--><!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information used to start the UIExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |

## requestModalUIExtensionWithAccount

ArkTS-Dyn:
```TypeScript
requestModalUIExtensionWithAccount(pickerWant: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>
```

Requests the specified foreground application to start the UIExtensionAbility of the corresponding type for the specified user. This API uses a promise to return the result. It can be called only on the main thread.The foreground application is specified by **bundleName** in **want.parameters**. If **bundleName** is left unspecified, or if the application specified by **bundleName** is not running in the foreground or does not exist,the UIExtensionAbility is directly started on the system UI. The UIExtensionAbility to start is determined by the combination of the **bundleName**, **abilityName**, and **moduleName** fields in **want**, and its type is determined by the **ability.want.params.uiExtensionType** field in **want.parameters**.

Before starting the UIExtensionAbility, ensure that the foreground application has finished page initialization.Otherwise, the UIExtensionAbility fails to start and the error message "uiContent is nullptr" is displayed. The application can determine the time to start the UIExtensionAbility by listening for the page loading status. After the page initialization is successful, the key log information "UIContentImpl: focus again" is recorded.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information used to start the UIExtensionAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | The account to request. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1.Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. 4.The logical screen corresponding to the specified accountId is not in the foreground. |

## setMissionIcon

```TypeScript
setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void
```

Sets an icon for this UIAbility in the mission. The maximum size of the icon is 600 MB. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | image.PixelMap | Yes | Icon of the UIAbility to set. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## setMissionIcon

```TypeScript
setMissionIcon(icon: image.PixelMap): Promise<void>
```

Sets an icon for this UIAbility in the mission. The maximum size of the icon is 600 MB. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap): Promise<void>--><!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | image.PixelMap | Yes | Icon of the UIAbility to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void
```

Starts a UIAbility with the caller information specified. The caller information is carried in **want** and identified at the system service layer. The UIAbility can obtain the caller information from the **want** parameter in the **onCreate** lifecycle callback. When this API is used to start a UIAbility, the caller information carried in **want** is not overwritten by the current application information. The system service layer can obtain the initial caller information. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

Starts a UIAbility with the caller information and start options specified. The caller information is carried in  
**want** and identified at the system service layer. The UIAbility can obtain the caller information from the  
**want** parameter in the **onCreate** lifecycle callback. When this API is used to start a UIAbility, the caller information carried in **want** is not overwritten by the current application information. The system service layer can obtain the initial caller information. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters used for starting the UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>
```

Starts a UIAbility with the caller information specified. The caller information is carried in **want** and identified at the system service layer. The UIAbility can obtain the caller information from the **want** parameter in the **onCreate** lifecycle callback. When this API is used to start a UIAbility, the caller information carried in **want** is not overwritten by the current application information. The system service layer can obtain the initial caller information. This API uses a promise to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters used for starting the UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityByCallWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityByCallWithAccount(want: Want, accountId: number): Promise<Caller>
```

ArkTS-Sta:
```TypeScript
startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>
```

Starts a UIAbility with the account ID specified and obtains the caller object for communicating with the UIAbility. This API can be called only on the main thread. This API uses a promise to return the result.This API cannot be used to start the UIAbility with the launch type set to  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.Observe the following when using this API:

- If an application needs to call this API to start a UIAbility that belongs to another user, it must have the  
ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION and ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS permissions.  
- If an application running in the background needs to call this API to start a UIAbility, it must have the  
ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission.  
- If **exported** of the target UIAbility is **false** in cross-application scenarios, the caller must have the  
ohos.permission.START\_INVISIBLE\_ABILITY permission.  
- The rules for using this API in the same-device and cross-device scenarios are different. For details, see  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ABILITY_BACKGROUND_COMMUNICATION and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>--><!--Device-UIAbilityContext-startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the UIAbility to start, including **abilityName**, **moduleName**, **bundleName**, **deviceId** (optional), and **parameters** (optional). If **deviceId** is left blank or null, the local UIAbility is started. If **parameters** is left blank or null, the UIAbility is started in the background. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. The value **-1** indicates the current user. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Promise used to return the caller object to communicate with. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: number, callback: AsyncCallback<AbilityResult>): void
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void
```

Starts a UIAbility with the account ID specified and returns the result when the UIAbility is terminated. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **data** is the result code and data when the UIAbility is terminated. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(
    want: Want,
    accountId: number,
    options: StartOptions,
    callback: AsyncCallback<void>
  ): void
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(
    want: Want,
    accountId: int,
    options: StartOptions,
    callback: AsyncCallback<void>
  ): void
```

Starts a UIAbility with the account ID and start options specified and returns the result when the UIAbility is terminated. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(    want: Want,    accountId: int,    options: StartOptions,    callback: AsyncCallback<void>  ): void--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(    want: Want,    accountId: int,    options: StartOptions,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters used for starting the UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: number, options?: StartOptions): Promise<AbilityResult>
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>
```

Starts a UIAbility with the account ID specified and returns the result when the UIAbility is terminated. This API uses a promise to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters used for starting the UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Promise that contains the **AbilityResult** parameter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

Starts a UIAbility with want and the account ID specified. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, options: StartOptions, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void
```

Starts a UIAbility with want, the account ID, and start options specified. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters used for starting the UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, options?: StartOptions): Promise<void>
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>
```

Starts a UIAbility with want, the account ID, and start options specified. This API uses a promise to return the result. It can be called only on the main thread.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters used for starting the UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, callback: AsyncCallback<void>): void
```

Starts a UIAbility. If the UIAbility has multiple instances, the latest instance is started. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    - For a successful launch in cross-device scenarios, the caller and target must be the same application and the  
    application must have the ohos.permission.DISTRIBUTED\_DATASYNC permission.  
    
    - If **visible** of the target UIAbility is **false** in cross-application scenarios, the caller must have the  
    ohos.permission.START\_INVISIBLE\_ABILITY permission.  
    
    - If the specified UIAbility has multiple instances, the caller must have the  
    ohos.permission.START\_RECENT\_ABILITY permission (available only for system applications) to start the latest  
    instance.  
    
    - If the caller is running in the background, the ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission is  
    required (available only for system applications).  
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startRecentAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

Starts a UIAbility with the start options specified. If the UIAbility has multiple instances, the latest instance is started. This API uses an asynchronous callback to return the result. It can be called only on the main thread.
    **NOTE**  
    
    - For a successful launch in cross-device scenarios, the caller and target must be the same application and the  
    application must have the ohos.permission.DISTRIBUTED\_DATASYNC permission.  
    
    - If **visible** of the target UIAbility is **false** in cross-application scenarios, the caller must have the  
    ohos.permission.START\_INVISIBLE\_ABILITY permission.  
    
    - If the specified UIAbility has multiple instances, the caller must have the  
    ohos.permission.START\_RECENT\_ABILITY permission (available only for system applications) to start the latest  
    instance.  
    
    - If the caller is running in the background, the ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission is  
    required (available only for system applications).  
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters used for starting the UIAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts a UIAbility. If the UIAbility has multiple instances, the latest instance is started. This API uses a promise to return the result. It can be called only on the main thread.
    **NOTE**  
    
    - For a successful launch in cross-device scenarios, the caller and target must be the same application and the  
    application must have the ohos.permission.DISTRIBUTED\_DATASYNC permission.  
    
    - If **visible** of the target UIAbility is **false** in cross-application scenarios, the caller must have the  
    ohos.permission.START\_INVISIBLE\_ABILITY permission.  
    
    - If the specified UIAbility has multiple instances, the caller must have the  
    ohos.permission.START\_RECENT\_ABILITY permission (available only for system applications) to start the latest  
    instance.  
    
    - If the caller is running in the background, the ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission is  
    required (available only for system applications).  
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startRecentAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters used for starting the UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000010](../../errorcode-ability.md#16000010-continuation-flag-is-forbidden) | The call with the continuation and prepare continuation flag is forbidden. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000053](../../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000055](../../errorcode-ability.md#16000055-installationfree-timeout) | Installation-free timed out. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000073](../../errorcode-ability.md#16000073-appcloneindex-is-invalid) | The app clone index is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000071](../../errorcode-ability.md#16000071-application-clone-is-not-supported) | App clone is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000072](../../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) | App clone or multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000076](../../errorcode-ability.md#16000076-appinstancekey-does-not-exist) | The app instance key is invalid.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000077](../../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) | The number of app instances reaches the limit.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000078](../../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) | The multi-instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000079](../../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) | The APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_INSTANCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_KEY cannot be specified.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |
| [16000080](../../errorcode-ability.md#16000080-new-instances-cannot-be-created) | Creating a new instance is not supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void
```

Starts a ServiceExtensionAbility. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for starting the ServiceExtensionAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

Starts a ServiceExtensionAbility. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for starting the ServiceExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

## startServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

Starts a ServiceExtensionAbility with the account ID specified. This API uses an asynchronous callback to return the result.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for starting the ServiceExtensionAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

## startServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>
```

Starts a ServiceExtensionAbility with the account ID specified. This API uses a promise to return the result.
    **NOTE**  
    
    For details about the startup rules for the components in the stage model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for starting the ServiceExtensionAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000019](../../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) | No matching ability is found.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |

## stopServiceExtensionAbility

```TypeScript
stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void
```

Stops a ServiceExtensionAbility. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for stopping the ServiceExtensionAbility. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000012](../../errorcode-ability.md#16000012-application-under-control) | The application is controlled.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000013](../../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## stopServiceExtensionAbility

```TypeScript
stopServiceExtensionAbility(want: Want): Promise<void>
```

Stops a ServiceExtensionAbility in the same application. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for stopping the ServiceExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## stopServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

Stops a ServiceExtensionAbility with the account ID specified in the same application. This API uses an asynchronous callback to return the result.
    **NOTE**  
    
    Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for stopping the ServiceExtensionAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

## stopServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>
```

Stops a ServiceExtensionAbility with the account ID specified in the same application. This API uses a promise to return the result.
    **NOTE**  
    
    Permission verification is not required when **accountId** specifies the current user.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information for stopping the ServiceExtensionAbility. |
| accountId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | ID of a system account. For details, see [getCreatedOsAccountsCount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000005](../../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000011](../../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16200001](../../errorcode-ability.md#16200001-caller-released) | The caller has been released. |
| [16000004](../../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 10 and later |

