# PhotoEditorExtensionContext

The context of Photo Editor extension. It allows access to PhotoEditorExtension-specific resources.

**继承/实现关系：** PhotoEditorExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class PhotoEditorExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

## saveEditedContentWithImage

```TypeScript
saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>
```

Save image data by image pixmap.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixeMap | image.PixelMap | 是 | Image pixmap. |
| option | image.PackingOption | 是 | Option for image packing. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Returns the result of save. |

**错误码：**

| 错误码ID | 错误信息 |
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>--><!--Device-PhotoEditorExtensionContext-saveEditedContentWithUri(uri: string): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | Image editing URI. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Returns the result of save. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 29600003 | Image too big. |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. &lt;br&gt;2.Incorrect parameter types. |
| 29600002 | Image input error. |
| 29600001 | Internal error. |

