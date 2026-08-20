# GridObjectSortComponent

网格对象排序组件，用于网格对象的编辑、拖动排序、新增和删除。

> **说明：**
> 
> - 该组件仅可在Stage模型下使用。
> 
> - 如果GridObjectSortComponent设置通用属性和 &gt; 通用事件，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到 &gt; GridObjectSortComponent本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议GridObjectSortComponent设置通用属性和通用事件。

**起始版本：** 11

<!--Device-unnamed-export declare struct GridObjectSortComponent--><!--Device-unnamed-export declare struct GridObjectSortComponent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { GridObjectSortComponentType, GridObjectSortComponentItem, GridObjectSortComponentOptions, GridObjectSortComponent } from '@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

Build function of GridObjectSortComponent.

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-GridObjectSortComponent-build(): void--><!--Device-GridObjectSortComponent-build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dataList

```TypeScript
dataList: Array<GridObjectSortComponentItem>
```

传入的数据，最大长度为50，数据长度超过50，只会取前50条数据。

**类型：** Array&lt;[GridObjectSortComponentItem](../../apis-default/arkts-apis/arkts-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentitem-i.md)&gt;

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-GridObjectSortComponent-dataList: Array<GridObjectSortComponentItem>--><!--Device-GridObjectSortComponent-dataList: Array<GridObjectSortComponentItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel: () => void
```

取消保存数据的回调。

**类型：** () =&gt; void

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-GridObjectSortComponent-onCancel: () => void--><!--Device-GridObjectSortComponent-onCancel: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onSave

```TypeScript
onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void
```

保存编辑排序的回调函数，select为编辑后的选中数据，unselect为编辑后的未选中数据。

**类型：** (select: Array&lt;[GridObjectSortComponentItem](../../apis-default/arkts-apis/arkts-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentitem-i.md)&gt;, unselect: Array&lt;GridObjectSortComponentItem&gt;) =&gt; void

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-GridObjectSortComponent-onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void--><!--Device-GridObjectSortComponent-onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Prop
  options: GridObjectSortComponentOptions
```

组件配置信息。

**类型：** [GridObjectSortComponentOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentoptions-i.md)

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-GridObjectSortComponent-@Prop  options: GridObjectSortComponentOptions--><!--Device-GridObjectSortComponent-@Prop  options: GridObjectSortComponentOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

