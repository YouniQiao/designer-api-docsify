# SceneResource

定义被其他3D资源扩展的场景资源.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface SceneResource--><!--Device-unnamed-export interface SceneResource-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## destroy

```TypeScript
destroy(): void
```

销毁场景资源，释放所有关联的资源或引用，一旦被释放，资源就不能被再次使用或访问。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SceneResource-destroy(): void--><!--Device-SceneResource-destroy(): void-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

场景资源名称，没有特殊格式要求。

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SceneResource-name: string--><!--Device-SceneResource-name: string-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## resourceType

```TypeScript
readonly resourceType: SceneResourceType
```

场景资源类型，默认值为undefined。

**类型：** SceneResourceType

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SceneResource-readonly resourceType: SceneResourceType--><!--Device-SceneResource-readonly resourceType: SceneResourceType-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

## uri

```TypeScript
readonly uri?: ResourceStr
```

需要加载的场景资源URI，默认值为undefined。

**类型：** ResourceStr

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-SceneResource-readonly uri?: ResourceStr--><!--Device-SceneResource-readonly uri?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUi.Graphics3D

