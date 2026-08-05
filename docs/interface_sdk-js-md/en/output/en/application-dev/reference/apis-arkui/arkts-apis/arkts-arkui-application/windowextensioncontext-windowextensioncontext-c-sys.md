# WindowExtensionContext (System API)

The WindowExtensionContext module provides the context environment for the WindowExtensionAbility. It inherits from [ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. The module provides the capabilities of the [WindowExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, including starting the ability. > **NOTE** > > - This module is deprecated since API version 21. You are advised to use > [UIExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ instead. > > - The APIs provided by this module are system APIs. > > - The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** WindowExtensionContext extends [ExtensionContext](../../../apis-ability-kit/arkts-apis/arkts-ability-application/extensioncontext-extensioncontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

<!--Device-unnamed-declare class WindowExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class WindowExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

Starts an ability. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-WindowExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target ability. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameters used for starting the ability. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts an ability. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-WindowExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target ability, such as the ability name and bundle name. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parameters used for starting the ability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 12 and later |
| [401](../../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

