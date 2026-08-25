# AccessibilityElement

无障碍节点元素，提供查询父/子元素、按内容或焦点方向查找元素、执行无障碍操作等能力，适用于无障碍辅助应用需要与界面节点交互和操作的场景。调用AccessibilityElement的方法前，先通过 [AccessibilityExtensionContext.getAccessibilityFocusedElement()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getaccessibilityfocusedelement) 或[AccessibilityExtensionContext.getRootInActiveWindow()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getrootinactivewindow) 获取AccessibilityElement实例。

**起始版本：** 9

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## enableScreenCurtain

```TypeScript
enableScreenCurtain(isEnable: boolean): void
```

开启或关闭幕帘屏。幕帘屏开启后，屏幕显示内容将被隐藏（屏幕变暗），但设备仍可正常响应操作。

**起始版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isEnable](#isenable) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300003](../errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## executeAction

```TypeScript
executeAction(action: AccessibilityAction, parameters?: Parameter): Promise<void>
```

根据action指定的操作类型和parameters，对无障碍节点元素执行相应操作。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| action | [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md) | 是 |
| parameters | [Parameter](arkts-accessibility-accessibilityextensioncontext-parameter-c-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300005](../errorcode-accessibility.md#9300005-不支持该操作) |

## findElement('textType')

```TypeScript
findElement(type: 'textType', condition: string): Promise<Array<AccessibilityElement>>
```

根据组件配置的accessibilityTextHint无障碍文本类型查询所有节点元素。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [type](#type) | 'textType' | 是 |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## findElement('elementId')

```TypeScript
findElement(type: 'elementId', condition: number): Promise<AccessibilityElement>
```

根据elementId查询当前活动窗口下的节点元素。使用Promise异步回调。与[findElementById](#findelementbyid)均根据元素ID查找节点元素，功能等价，推荐优先使用findElementById。

**起始版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [type](#type) | 'elementId' | 是 |
| condition | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## findElementByContent

```TypeScript
findElementByContent(condition: string): Promise<Array<AccessibilityElement>>
```

根据元素的内容文本查找节点元素，将返回包含指定文本的所有节点元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection): Promise<AccessibilityElement>
```

根据焦点方向查找元素。使用Promise异步回调。与 [findElementsByCondition](#findelementsbycondition) 相比，本方法主要用于查找Web组件；findElementsByCondition主要用于查找UI组件。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |

## findElementByFocusDirection

```TypeScript
findElementByFocusDirection(condition: FocusDirection, type: FocusRuleType): Promise<AccessibilityElement>
```

根据焦点方向和聚焦类型查找元素。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | 是 |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |

## findElementById

```TypeScript
findElementById(condition: number): Promise<AccessibilityElement>
```

根据元素ID查找当前活动窗口下的节点元素。使用Promise异步回调。与[findElement('elementId')](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md#findelementcontent)功能等价，推荐优先使用本 方法。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |

## findElementsByAccessibilityHintText

```TypeScript
findElementsByAccessibilityHintText(condition: string): Promise<Array<AccessibilityElement>>
```

根据提示文本查找元素，将返回accessibilityTextHint属性匹配该文本的所有节点元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition): Promise<FocusMoveResult>
```

查询满足条件的可聚焦节点。使用Promise异步回调。与[findElementByFocusDirection](#findelementbyfocusdirection)相 比，本方法主要用于查找UI组件；findElementByFocusDirection主要用于查找Web组件。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | 是 |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## findElementsByCondition

```TypeScript
findElementsByCondition(rule: FocusRule, condition: FocusCondition, type: FocusRuleType): Promise<FocusMoveResult>
```

根据规则和查询条件查找目标类型的可聚焦节点。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | [FocusRule](arkts-accessibility-focusrule-t-sys.md) | 是 |
| condition | [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | 是 |
| [type](#type) | [FocusRuleType](arkts-accessibility-accessibility-focusruletype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FocusMoveResult](arkts-accessibility-accessibilityextensioncontext-focusmoveresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getChildren

```TypeScript
getChildren(): Promise<Array<AccessibilityElement>>
```

获取元素的子元素列表。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getCursorPosition

```TypeScript
getCursorPosition(callback: AsyncCallback<number>): void
```

获取文本组件中光标位置。使用callback异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## getCursorPosition

```TypeScript
getCursorPosition(): Promise<number>
```

获取文本组件中光标位置。使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

## getParent

```TypeScript
getParent(): Promise<AccessibilityElement>
```

获取无障碍节点元素的父元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getRoot

```TypeScript
getRoot(): Promise<AccessibilityElement>
```

获取活动窗口中的根元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## accessibilityFocused

```TypeScript
accessibilityFocused?: boolean
```

表示元素是否因无障碍目的获得焦点。true表示已获得焦点，false表示未获得焦点。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityGroup

```TypeScript
accessibilityGroup?: boolean
```

元素是否为无障碍组。true表示元素是无障碍组，false表示元素不是无障碍组。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

组件的无障碍级别。'auto'：当前组件由无障碍分组服务和ArkUI进行综合判断组件是否可被辅助功能识别。'yes'：当前组件可被辅助功能识别。'no'：当前组件不可被辅助功能识别。'no-hide-descendants'：当前组件及其所有子组件不可被辅助功能识别。默认值：'auto'。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId?: number
```

下一个要获得焦点的组件的ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityPreviousFocusId

```TypeScript
accessibilityPreviousFocusId?: number
```

上一个要获得焦点的组件的ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityScrollable

```TypeScript
accessibilityScrollable?: boolean
```

元素是否因无障碍目的而可滚动。优先级高于scrollable，即当accessibilityScrollable与scrollable取值冲突时以accessibilityScrollable为准。true表示元素可滚动，false表示元素不可滚动。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription?: string
```

元素的自定义无障碍状态播报文本信息。

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityText

```TypeScript
accessibilityText?: string
```

元素的无障碍文本信息。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## accessibilityVisible

```TypeScript
accessibilityVisible?: boolean
```

组件是否无障碍可见。true表示可见，false表示不可见。默认值：true。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## belongTreeId

```TypeScript
belongTreeId?: number
```

表示元素所属的组件树ID。默认值为-1。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## bundleName

```TypeScript
bundleName?: string
```

包名。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## checkable

```TypeScript
checkable?: boolean
```

元素是否可勾选。true表示可勾选，false表示不可勾选。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## checked

```TypeScript
checked?: boolean
```

元素是否已勾选。true表示已勾选，false表示未勾选。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## childrenIds

```TypeScript
childrenIds?: Array<number>
```

组件的子元素ID列表。默认值：空数组。

**类型：** Array&lt;number&gt;

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## childrenTreeId

```TypeScript
childrenTreeId?: number
```

表示元素的子组件树ID。默认值为-1。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## clickable

```TypeScript
clickable?: boolean
```

元素是否可点击。true表示可点击，false表示不可点击。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## clip

```TypeScript
clip?: boolean
```

组件是否需要裁剪。true表示需要裁剪，false表示不需要裁剪。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## componentId

```TypeScript
componentId?: number
```

元素所属组件的ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## componentType

```TypeScript
componentType?: string
```

元素所属组件的类型。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## contents

```TypeScript
contents?: Array<string>
```

元素显示内容。默认值：空数组。

**类型：** Array&lt;string&gt;

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## currentIndex

```TypeScript
currentIndex?: number
```

当前项的索引。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## currentItem

```TypeScript
currentItem?: AccessibilityGrid
```

组件网格中的当前项。

**类型：** [AccessibilityGrid](arkts-accessibility-accessibilityextensioncontext-accessibilitygrid-i-sys.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## customActions

```TypeScript
customActions?: Array<string>
```

元素支持的自定义操作列表。

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## customComponentType

```TypeScript
customComponentType?: string
```

自定义组件类型。与元素的[AccessibilityRoleType](../../apis-arkui/arkts-components/arkts-arkui-accessibilityroletype-e.md)类型所对应。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## description

```TypeScript
description?: string
```

元素的描述信息。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## editable

```TypeScript
editable?: boolean
```

元素是否可编辑。true表示可编辑，false表示不可编辑。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## endIndex

```TypeScript
endIndex?: number
```

屏幕上显示的最后一个列表项的索引。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## error

```TypeScript
error?: string
```

元素的错误状态。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## extraInfo

```TypeScript
extraInfo?: string
```

元素的额外信息。值为JSON字符串。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## focusable

```TypeScript
focusable?: boolean
```

元素是否可获得焦点（此处指无障碍焦点，与输入焦点不同）。true表示可获得焦点，false表示不可获得焦点。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## hintText

```TypeScript
hintText?: string
```

提示文本。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## hotArea

```TypeScript
hotArea?: Rect
```

元素的可触摸区域。

**类型：** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## inputType

```TypeScript
inputType?: number
```

输入文本的类型，不同数值对应不同的输入模式：0表示无特定类型；1表示文本；2表示邮箱；3表示日期；4表示时间；5表示数字；6表示密码；7表示电话号码；8表示用户名；9表示新密码。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## inspectorKey

```TypeScript
inspectorKey?: string
```

检查器键。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isActive

```TypeScript
isActive?: boolean
```

元素是否处于活动状态。true表示活动状态，false表示非活动状态。默认值：true。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isEnable

```TypeScript
isEnable?: boolean
```

元素是否启用。true表示启用，false表示未启用。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isEssential

```TypeScript
isEssential?: boolean
```

表示元素对用户是否是必需的。true表示元素是必需的，false表示元素不是必需的，默认值为false。

**类型：** boolean

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isFocused

```TypeScript
isFocused?: boolean
```

表示元素是否已获得焦点（此处指无障碍焦点，与输入焦点不同）。true表示已获得焦点，false表示未获得焦点。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isHint

```TypeScript
isHint?: boolean
```

元素是否为提示信息。true表示元素是提示信息，false表示非提示信息。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isPassword

```TypeScript
isPassword?: boolean
```

元素是否为密码。true表示元素是密码，false表示不是密码。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## isVisible

```TypeScript
isVisible?: boolean
```

元素是否可见。true表示元素可见，false表示元素不可见。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## itemCount

```TypeScript
itemCount?: number
```

项目总数。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## lastContent

```TypeScript
lastContent?: string
```

最后一项内容。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## layer

```TypeScript
layer?: number
```

元素的显示层级。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## longClickable

```TypeScript
longClickable?: boolean
```

元素是否可长按。true表示可长按，false表示不可长按。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## mainWindowId

```TypeScript
mainWindowId?: number
```

组件的主窗口ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## navDestinationId

```TypeScript
navDestinationId?: number
```

组件的导航目标ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## offset

```TypeScript
offset?: number
```

内容区域相对于可滚动组件（如List和Grid）顶部坐标的像素偏移量，单位为像素（px）。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## pageId

```TypeScript
pageId?: number
```

页面ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## parentId

```TypeScript
parentId?: number
```

组件的父元素ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## pluralLineSupported

```TypeScript
pluralLineSupported?: boolean
```

表示元素是否支持多行文本。true表示支持，false表示不支持。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## rect

```TypeScript
rect?: Rect
```

元素的区域。

**类型：** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## resourceName

```TypeScript
resourceName?: string
```

元素的资源名称。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## screenRect

```TypeScript
screenRect?: Rect
```

元素的显示区域。

**类型：** [Rect](arkts-accessibility-accessibilityextensioncontext-rect-i.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## scrollable

```TypeScript
scrollable?: boolean
```

元素是否可滚动。true表示元素可滚动，false表示不可滚动。当与accessibilityScrollable取值冲突时，以accessibilityScrollable为准。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## selected

```TypeScript
selected?: boolean
```

元素是否已选中。true表示已选中，false表示未选中。默认值：false。

**类型：** boolean

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## sourceType

```TypeScript
sourceType?: AccessibilitySourceType
```

组件来源类型，用于区分默认组件和新增、修改的虚拟组件。

**类型：** [AccessibilitySourceType](arkts-accessibility-accessibility-accessibilitysourcetype-e-sys.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## spans

```TypeScript
spans?: AccessibilitySpan[]
```

组件的辅助功能超链接文本信息数组。默认值：空数组。

**类型：** [AccessibilitySpan](arkts-accessibility-accessibilityextensioncontext-accessibilityspan-i-sys.md)[]

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## startIndex

```TypeScript
startIndex?: number
```

屏幕上第一个列表项的索引。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## supportedActionNames

```TypeScript
supportedActionNames?: Array<string>
```

支持的操作名称。默认值：空数组。

**类型：** Array&lt;string&gt;

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## text

```TypeScript
text?: string
```

元素的文本内容。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## textLengthLimit

```TypeScript
textLengthLimit?: number
```

元素的最大文本长度。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## textMoveUnit

```TypeScript
textMoveUnit?: accessibility.TextMoveUnit
```

文本朗读时的移动单位。默认值：char。

**类型：** accessibility.TextMoveUnit

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## textType

```TypeScript
textType?: string
```

元素的无障碍文本类型，由组件的accessibilityTextHint属性配置。

**类型：** string

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## triggerAction

```TypeScript
triggerAction?: AccessibilityAction
```

触发元素事件的操作。

**类型：** [AccessibilityAction](arkts-accessibility-accessibility-accessibilityaction-e-sys.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type?: WindowType
```

元素的窗口类型。

**类型：** [WindowType](arkts-accessibility-windowtype-t.md)

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## valueMax

```TypeScript
valueMax?: number
```

最大值。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## valueMin

```TypeScript
valueMin?: number
```

最小值。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## valueNow

```TypeScript
valueNow?: number
```

当前值。默认值：0。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## windowId

```TypeScript
windowId?: number
```

窗口ID。默认值：-1。

**类型：** number

**起始版本：** 20

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。
