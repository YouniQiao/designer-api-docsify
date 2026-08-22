# SubHeaderV2OperationItem

操作区的设置项。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class SubHeaderV2OperationItem--><!--Device-unnamed-export declare class SubHeaderV2OperationItem-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(options: SubHeaderV2OperationItemOptions)
```

操作项SubHeaderV2OperationItem的构造函数。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-constructor(options: SubHeaderV2OperationItemOptions)--><!--Device-SubHeaderV2OperationItem-constructor(options: SubHeaderV2OperationItemOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubHeaderV2OperationItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-subheaderv2-subheaderv2operationitemoptions-i.md) | 是 | 操作项配置信息。用于构建SubHeaderV2OperationItem对象。 |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

子标题右侧操作项无障碍说明，用于为用户进一步说明当前组件。

默认值：“单指双击即可执行”。

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityDescription?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel?: string
```

子标题右侧操作项无障碍重要性。

支持的值为：

"auto"：当前子标题右侧操作项由无障碍分组服务和ArkUI进行综合判断是否可被无障碍辅助服务所识别。

"yes"：当前子标题右侧操作项可被无障碍辅助服务所识别。

"no"：当前子标题右侧操作项不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前子标题右侧操作项及其所有子组件不可被无障碍辅助服务所识别。

默认值：“yes”。

**类型：** string

**默认值：** "auto".The options are as follows:<br/> "auto":The value is converted to "yes" or "no" based on the component. "yes": the current component is selectable for the accessibility service. "no": The current component is not selectable for the accessibility service. "no-hide-descendants":The current component and all its child components are not selectable<br/> for the accessibility service.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityLevel?: string--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityLevel?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

子标题右侧操作项无障碍描述。

默认值：undefined

**类型：** [ResourceStr](arkts-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityText?: ResourceStr--><!--Device-SubHeaderV2OperationItem-@Trace  public accessibilityText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  public action?: SubHeaderV2OperationItemAction
```

操作区事件回调。默认值：() =&gt; void。

**类型：** [SubHeaderV2OperationItemAction](../../apis-arkui/arkts-apis/arkts-arkui-subheaderv2operationitemaction-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public action?: SubHeaderV2OperationItemAction--><!--Device-SubHeaderV2OperationItem-@Trace  public action?: SubHeaderV2OperationItemAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Trace
  public content: SubHeaderV2OperationItemType
```

操作区元素内容。

**类型：** [SubHeaderV2OperationItemType](../../apis-arkui/arkts-apis/arkts-arkui-subheaderv2operationitemtype-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public content: SubHeaderV2OperationItemType--><!--Device-SubHeaderV2OperationItem-@Trace  public content: SubHeaderV2OperationItemType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
@Trace
  public defaultFocus?: boolean
```

子标题右侧操作项是否为默认焦点。

true：子标题右侧操作项是默认焦点。

false：子标题右侧操作项不是默认焦点。

默认值：false

**类型：** boolean

**默认值：** false

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public defaultFocus?: boolean--><!--Device-SubHeaderV2OperationItem-@Trace  public defaultFocus?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
@Trace
  public id?: string
```

子标题右侧操作项id。需要为子标题右侧操作项设置id的时候设置此参数，缺省时不设置此参数。

默认值：undefined，表示不设置子标题右侧操作项id。

**类型：** string

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SubHeaderV2OperationItem-@Trace  public id?: string--><!--Device-SubHeaderV2OperationItem-@Trace  public id?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

