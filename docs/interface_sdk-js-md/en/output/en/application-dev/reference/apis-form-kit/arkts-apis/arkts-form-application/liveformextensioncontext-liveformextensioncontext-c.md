# LiveFormExtensionContext

**LiveFormExtensionContext**, inherited from [ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, is the context of [LiveFormExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Inheritance/Implementation:** LiveFormExtensionContext extends [ExtensionContext](../../../apis-ability-kit/arkts-apis/arkts-ability-application/extensioncontext-extensioncontext-c.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## startAbilityByLiveForm

```TypeScript
startAbilityByLiveForm(want: Want): Promise<void>
```

Starts the widget provider (application) page. This API uses a promise to return the result. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_This API can only be used to start the page of the interactive widget provider (application). If this API is used to start the page of another application, error code 16501011 will be reported. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_You are advised to call this API in click event callbacks. Calling it in callbacks of other gesture events is not recommended, and direct calls in non-gesture events are not allowed. Otherwise, the error code 16501011 will be reported. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_In addition, this API can be directly called in the click event callback but cannot be called after a delay. Otherwise, the error code 16501011 will be reported.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LiveFormExtensionContext-startAbilityByLiveForm(want: Want): Promise<void>--><!--Device-LiveFormExtensionContext-startAbilityByLiveForm(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the application page to be started.\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported due to limited device capabilities. |
| [16500050](../../errorcode-form.md#16500050-ipc-failure) | An IPC connection error happened. |
| [16500100](../../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |
| [16501000](../../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16501011](../../errorcode-form.md#16501011-api-not-supported) | The form can not support this operation |

