# FolderStackAttribute

The FolderStackAttribute.@extends CommonMethod @interface FolderStackAttribute

**继承/实现关系：** FolderStackAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alignContent

```TypeScript
default alignContent(value: Alignment | undefined): this
```

设置子组件在容器内的对齐方式。 该属性与align同时设置时，后设置的属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Alignment](arkts-arkui-alignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<FolderStackAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## autoHalfFold

```TypeScript
default autoHalfFold(value: boolean | undefined): this
```

设置是否开启自动旋转，仅在系统自动旋转关闭时该属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## enableAnimation

```TypeScript
default enableAnimation(value: boolean | undefined): this
```

设置是否使用默认动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## onFolderStateChange

```TypeScript
default onFolderStateChange(callback: OnFoldStatusChangeCallback | undefined): this
```

当前设备的折叠状态改变时触发回调，仅在横屏状态下生效。Anonymous Object Rectification

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnFoldStatusChangeCallback](arkts-arkui-onfoldstatuschangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## onHoverStatusChange

```TypeScript
default onHoverStatusChange(handler: OnHoverStatusChangeCallback | undefined): this
```

当前设备的悬停状态改变时触发回调。Anonymous Object Rectification

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnHoverStatusChangeCallback](arkts-arkui-onhoverstatuschangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |

## setFolderStackOptions

```TypeScript
default setFolderStackOptions(options?: FolderStackOptions): this
```

Set FolderStack options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FolderStackOptions](arkts-arkui-folderstack-folderstackoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [FolderStackAttribute](arkts-arkui-folderstack-folderstackattribute-i.md) |
