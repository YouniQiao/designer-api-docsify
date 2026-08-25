# AccessibilityElement

无障碍节点元素，提供查询父/子元素、按内容或焦点方向查找元素、执行无障碍操作等能力，适用于无障碍辅助应用需要与界面节点交互和操作的场景。调用AccessibilityElement的方法前，先通过 [AccessibilityExtensionContext.getAccessibilityFocusedElement()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getaccessibilityfocusedelement) 或[AccessibilityExtensionContext.getRootInActiveWindow()](arkts-accessibility-accessibilityextensioncontext-c-sys.md#getrootinactivewindow) 获取AccessibilityElement实例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## actionNames

```TypeScript
actionNames(callback: AsyncCallback<Array<string>>): void
```

获取节点元素支持的所有操作名称。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.actionNames().then((data: string[]) => {
  console.info(`succeeded in getting action names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get action names. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.actionNames((err: BusinessError, data: string[]) => {
  if (err) {
    console.error(`Failed to get action names. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in getting action names, ${JSON.stringify(data)}`);
});
```

## actionNames

```TypeScript
actionNames(): Promise<Array<string>>
```

获取节点元素支持的所有操作名称。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**示例**

参见 [actionNames](#actionnames)

## attributeNames

```TypeScript
attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void
```

获取节点元素的所有属性名称。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;T&gt;&gt; | 是 |

**示例**

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.attributeNames().then((data: ElementAttributeKeys[]) => {
  console.info(`succeeded in getting attribute names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get attribute names. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.attributeNames((err: BusinessError, data: ElementAttributeKeys[]) => {
  if (err) {
    console.error(`Failed to get attribute names. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in getting attribute names, ${JSON.stringify(data)}`);
});
```

## attributeNames

```TypeScript
attributeNames<T extends keyof ElementAttributeValues>(): Promise<Array<T>>
```

获取节点元素的所有属性名称。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

**示例**

参见 [attributeNames](#attributenames)

## attributeValue

```TypeScript
attributeValue<T extends keyof ElementAttributeValues>(
    attributeName: T,
    callback: AsyncCallback<ElementAttributeValues[T]>
  ): void
```

根据属性名称获取属性值。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attributeName | T | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ElementAttributeValues[T]&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300004](../errorcode-accessibility.md#9300004-属性不存在) |

**示例**

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.attributeValue(attributeName).then((data: string) => {
  console.info(`succeeded in getting attribute value by name, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get attribute value. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.attributeValue(attributeName, (err: BusinessError, data: string) => {
  if (err) {
    console.error(`Failed to get attribute value. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in getting attribute value, ${JSON.stringify(data)}`);
});
```

## attributeValue

```TypeScript
attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues[T]>
```

根据属性名称获取属性值。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attributeName | T | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ElementAttributeValues[T] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300004](../errorcode-accessibility.md#9300004-属性不存在) |

**示例**

参见 [attributeValue](#attributevalue)

## findElement('content')

```TypeScript
findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void
```

根据节点内容查询所有节点元素。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'content' | 是 |
| condition | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('content', condition, (err: BusinessError, data: AccessibilityElement[]) => {
  if (err) {
    console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
});
```

## findElement('content')

```TypeScript
findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>
```

根据节点内容查询所有节点元素。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'content' | 是 |
| condition | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('content', condition).then((data: AccessibilityElement[]) => {
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
});
```

## findElement('focusType')

```TypeScript
findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void
```

根据焦点元素类型查询节点元素。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusType' | 是 |
| condition | [FocusType](arkts-accessibility-focustype-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { FocusType, AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('focusType', condition, (err: BusinessError, data: AccessibilityElement) => {
  if (err) {
    console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
});
```

## findElement('focusType')

```TypeScript
findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>
```

根据焦点元素类型查询节点元素。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusType' | 是 |
| condition | [FocusType](arkts-accessibility-focustype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { FocusType, AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('focusType', condition).then((data: AccessibilityElement) => {
  console.info(`succeeded in finding element,${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
});
```

## findElement('focusDirection')

```TypeScript
findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void
```

根据下一焦点元素方向查询节点元素。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusDirection' | 是 |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { FocusDirection, AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('focusDirection', condition, (err: BusinessError, data: AccessibilityElement) => {
  if (err) {
    console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
});
```

## findElement('focusDirection')

```TypeScript
findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>
```

根据下一焦点元素方向查询节点元素。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'focusDirection' | 是 |
| condition | [FocusDirection](arkts-accessibility-focusdirection-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { FocusDirection, AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.findElement('focusDirection', condition).then((data: AccessibilityElement) => {
  console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
});
```

## performAction

```TypeScript
performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void
```

对无障碍节点元素执行指定操作。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [actionName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | string | 是 |
| parameters | object | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300005](../errorcode-accessibility.md#9300005-不支持该操作) |

**示例**

无参数Action。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
// Action描述中无明确要求的，均为无参数Action。
rootElement.performAction('click').then(() => {
  console.info(`succeeded in performing action.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to perform action. Code: ${err.code}, message: ${err.message}`);
});
```

有参数Action（setSelection）。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
// setSelection示例代码。
rootElement.performAction('setSelection', {
  selectTextBegin: '0', // 表示选择起始位置。
  selectTextEnd: '8',   // 表示选择结束位置。
  selectTextInForWard: true   // true表示为前光标，false表示为后光标。
}).then(() => {
  console.info(`succeeded in performing action`);
}).catch((err: BusinessError) => {
  console.error(`Failed to perform action. Code: ${err.code}, message: ${err.message}`);
});
```

有参数Action（setCursorPosition）。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
// setCursorPosition示例代码。
rootElement.performAction('setCursorPosition', {
  offset: '1'   // 表示光标的设置位置。
}).then(() => {
  console.info(`succeeded in performing action`);
}).catch((err: BusinessError) => {
  console.error(`Failed to perform action. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.performAction(actionName, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to perform action. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in performing action, actionName is ${actionName}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';
let parameters: object = {};

// rootElement是AccessibilityElement的实例，通过getFocusElement()或getWindowRootElement()获取
rootElement.performAction(actionName, parameters, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to perform action. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in performing action,actionName is ${actionName}, parameters is ${parameters}`);
});
```

## performAction

```TypeScript
performAction(actionName: string, parameters?: object): Promise<void>
```

对无障碍节点元素执行指定操作。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [actionName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | string | 是 |
| parameters | object | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300005](../errorcode-accessibility.md#9300005-不支持该操作) |

**示例**

参见 [performAction](#performaction)

## performAction

```TypeScript
performAction(actionName: string, callback: AsyncCallback<void>): void
```

对无障碍节点元素执行指定操作。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [actionName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [9300005](../errorcode-accessibility.md#9300005-不支持该操作) |

**示例**

参见 [performAction](#performaction)
