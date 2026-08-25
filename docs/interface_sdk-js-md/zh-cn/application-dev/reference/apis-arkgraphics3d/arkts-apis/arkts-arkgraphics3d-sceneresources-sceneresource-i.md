# SceneResource

用于表示场景中的资源。@interface SceneResource

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## destroy

```TypeScript
destroy(): void
```

销毁场景资源，释放所有关联的资源或引用，一旦被释放，资源就不能被再次使用或访问。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## name

```TypeScript
name: string
```

名称，没有特殊格式要求。

**类型：** string

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## resourceType

```TypeScript
readonly resourceType: SceneResourceType
```

场景资源类型，默认值为undefined。

**类型：** [SceneResourceType](arkts-arkgraphics3d-sceneresources-sceneresourcetype-e.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D

## uri

```TypeScript
readonly uri?: ResourceStr
```

需要加载的资源，默认值为undefined。

**类型：** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**起始版本：** 12

**系统能力：** SystemCapability.ArkUi.Graphics3D
