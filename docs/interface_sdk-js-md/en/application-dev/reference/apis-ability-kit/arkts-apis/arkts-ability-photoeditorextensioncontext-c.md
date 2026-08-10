# PhotoEditorExtensionContext

The context of Photo Editor extension. It allows access to PhotoEditorExtension-specific resources.

**Inheritance/Implementation:** PhotoEditorExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## saveEditedContentWithImage

```TypeScript
saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>
```

Save image data by image pixmap.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixeMap | image.PixelMap | Yes | Image pixmap. |
| option | image.PackingOption | Yes | Option for image packing. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Returns the result of save. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 29600003 | Image too big. |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. &lt;br&gt;2.Incorrect parameter types. |
| 29600002 | Image input error. |
| 29600001 | Internal error. |

## saveEditedContentWithUri

```TypeScript
saveEditedContentWithUri(uri: string): Promise<AbilityResult>
```

Save image data by uri.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Image editing URI. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Returns the result of save. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 29600003 | Image too big. |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. &lt;br&gt;2.Incorrect parameter types. |
| 29600002 | Image input error. |
| 29600001 | Internal error. |

