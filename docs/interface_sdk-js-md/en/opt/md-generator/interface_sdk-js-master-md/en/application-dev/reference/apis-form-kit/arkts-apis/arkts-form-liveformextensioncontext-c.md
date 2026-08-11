# LiveFormExtensionContext

**LiveFormExtensionContext**, inherited from   
[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md), is the context of   
[LiveFormExtensionAbility](arkts-app-form-liveformextensionability.md).

**Inheritance/Implementation:** LiveFormExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 20

<!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## startAbilityByLiveForm

```TypeScript
startAbilityByLiveForm(want: Want): Promise<void>
```

Starts the widget provider (application) page. This API uses a promise to return the result.&lt;br&gt;This API can only be used to start the page of the interactive widget provider (application). If this API is used to start the page of another application, error code 16501011 will be reported.&lt;br&gt;You are advised to call this API in click event callbacks. Calling it in callbacks of other gesture events is not recommended, and direct calls in non-gesture events are not allowed. Otherwise, the error code 16501011 will be reported.&lt;br&gt;In addition, this API can be directly called in the click event callback but cannot be called after a delay. Otherwise, the error code 16501011 will be reported.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LiveFormExtensionContext-startAbilityByLiveForm(want: Want): Promise<void>--><!--Device-LiveFormExtensionContext-startAbilityByLiveForm(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16501011](../errorcode-form.md#16501011-api-not-supported) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
