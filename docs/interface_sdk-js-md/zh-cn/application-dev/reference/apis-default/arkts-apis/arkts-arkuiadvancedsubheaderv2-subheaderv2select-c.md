# SubHeaderV2Select

下拉选择器配置项，包含下拉选项内容、选中状态及回调事件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class SubHeaderV2Select--><!--Device-unnamed-export declare class SubHeaderV2Select-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(options: SubHeaderV2SelectOptions)
```

select内容以及事件构造函数。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-public constructor(options: SubHeaderV2SelectOptions)--><!--Device-SubHeaderV2Select-public constructor(options: SubHeaderV2SelectOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2SelectOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedsubheaderv2-subheaderv2selectoptions-i.md) | 是 | 下拉选项信息。 |

## defaultFocus

```TypeScript
@Trace
  public defaultFocus?: boolean
```

下拉按钮是否为默认焦点。

true：下拉按钮是默认焦点。

false：下拉按钮不是默认焦点。

默认值：false

**类型：** boolean

**默认值：** false

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public defaultFocus?: boolean--><!--Device-SubHeaderV2Select-@Trace  public defaultFocus?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
@Trace
  public id?: string
```

下拉按钮id。需要为下拉按钮设置id的时候设置此参数，缺省时不设置此参数。

默认值：undefined，表示不设置下拉按钮id。

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public id?: string--><!--Device-SubHeaderV2Select-@Trace  public id?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onSelect

```TypeScript
@Trace
  public onSelect?: SubHeaderV2SelectOnSelect
```

下拉菜单选中某一项的回调。

默认值：undefined

**类型：** [SubHeaderV2SelectOnSelect](../../apis-arkui/arkts-apis/arkts-arkui-subheaderv2selectonselect-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public onSelect?: SubHeaderV2SelectOnSelect--><!--Device-SubHeaderV2Select-@Trace  public onSelect?: SubHeaderV2SelectOnSelect-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@Trace
  public options: SelectOption[]
```

下拉选项内容。

**类型：** [SelectOption](../arkts-components/arkts-select-selectoption-i.md)[]

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public options: SelectOption[]--><!--Device-SubHeaderV2Select-@Trace  public options: SelectOption[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedContent

```TypeScript
@Trace
  public selectedContent?: ResourceStr
```

设置下拉按钮本身的文本内容。默认值：'' 。从API version 20开始，支持Resource类型。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public selectedContent?: ResourceStr--><!--Device-SubHeaderV2Select-@Trace  public selectedContent?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Trace
  public selectedIndex?: int
```

设置下拉菜单初始选项的索引。

第一项的索引为0。

当不设置selectedIndex属性时，

默认选择值为-1，菜单项不选中。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2Select-@Trace  public selectedIndex?: int--><!--Device-SubHeaderV2Select-@Trace  public selectedIndex?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

