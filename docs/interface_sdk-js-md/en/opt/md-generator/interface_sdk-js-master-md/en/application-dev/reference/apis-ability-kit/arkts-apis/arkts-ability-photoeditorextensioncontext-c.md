# PhotoEditorExtensionContext

The context of Photo Editor extension. It allows access to PhotoEditorExtension-specific resources.

**Inheritance/Implementation:** PhotoEditorExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 12

<!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## saveEditedContentWithImage

```TypeScript
saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>
```

Save image data by image pixmap.

**Since:** 12

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixeMap | image.PixelMap | Yes |
| option | image.PackingOption | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [29600003](../errorcode-ability.md#29600003-image-too-large) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [29600002](../errorcode-ability.md#29600002-internal-error-during-image-editing) |
| [29600001](../errorcode-ability.md#29600001-internal-error-during-image-editing) |

## saveEditedContentWithUri

```TypeScript
saveEditedContentWithUri(uri: string): Promise<AbilityResult>
```

Save image data by uri.

**Since:** 12

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [29600003](../errorcode-ability.md#29600003-image-too-large) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [29600002](../errorcode-ability.md#29600002-internal-error-during-image-editing) |
| [29600001](../errorcode-ability.md#29600001-internal-error-during-image-editing) |
