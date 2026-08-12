# AccessibilityExtensionContext

辅助功能扩展的上下文环境，用来配置辅助应用关注信息类型、查询节点信息、手势注入等。

**继承/实现关系：** AccessibilityExtensionContext extends [ExtensionContext](ExtensionContext)

**起始版本：** 9

<!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AccessibilityExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## getAccessibilityFocusedElement

```TypeScript
getAccessibilityFocusedElement(): Promise<AccessibilityElement>
```

获取当前获得焦点的元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityFocusedElement(): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## 示例

```TypeScript
import {
  AccessibilityElement,
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    this.context.getAccessibilityFocusedElement().then((element: AccessibilityElement) => {
      console.info(`succeeded in getting accessibility focused element, ${element.bundleName}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to get accessibility focused element. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## getAccessibilityWindowsSync

```TypeScript
getAccessibilityWindowsSync(displayId?: number): Array<AccessibilityElement>
```

获取窗口列表。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getAccessibilityWindowsSync(displayId?: long): Array<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      let displayId: number = 0;
      let windowList = this.context.getAccessibilityWindowsSync(displayId);
      if (windowList) {
        for (let window of windowList) {
          console.info(`getAccessibilityWindowsSync: windowId: ${window.windowId}`);
        }
      }
    } catch (err) {
     console.error(`Failed to get accessibility windows sync. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## getDefaultFocusedElementIds

```TypeScript
getDefaultFocusedElementIds(windowId: number): Promise<Array<number>>
```

提供查询应用自定义默认焦点的能力。使用Promise异步回调。

**起始版本：** 18

<!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>--><!--Device-AccessibilityExtensionContext-getDefaultFocusedElementIds(windowId: int): Promise<Array<long>>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    let windowId: number = 10;

    this.context.getDefaultFocusedElementIds(windowId).then((data: number[]) => {
      console.info(`succeeded in getting default focus, ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to get default focus. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## getElements

```TypeScript
getElements(windowId: number, elementId?: number): Promise<Array<AccessibilityElement>>
```

提供批量查询节点的能力。使用Promise异步回调。

**起始版本：** 18

<!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>--><!--Device-AccessibilityExtensionContext-getElements(windowId: int, elementId?: long): Promise<Array<AccessibilityElement>>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| elementId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## 示例

```TypeScript
import {
  AccessibilityElement,
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    let windowId: number = 10;
    let elementId: number = 10;

    this.context.getElements(windowId, elementId).then((data:AccessibilityElement[]) => {
      console.info(`succeeded in finding element, ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to find element. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## getRootInActiveWindow

```TypeScript
getRootInActiveWindow(windowId?: number): Promise<AccessibilityElement>
```

获取活动窗口根元素。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>--><!--Device-AccessibilityExtensionContext-getRootInActiveWindow(windowId?: int): Promise<AccessibilityElement>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AccessibilityElement](arkts-accessibility-accessibilityextensioncontext-accessibilityelement-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [9300006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300006-目标应用和无障碍服务建立连接失败) |
| [9300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-accessibility-kit/errorcode-accessibility.md#9300003-不具备执行该操作的无障碍权限) |

## 示例

```TypeScript
import {
  AccessibilityElement,
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    let windowId: number = 0;

    this.context.getRootInActiveWindow(windowId).then((element: AccessibilityElement) => {
      console.info(`succeeded in getting root in active window element, ${element.bundleName}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to get root in active window element. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## holdRunningLockSync

```TypeScript
holdRunningLockSync(): void
```

持有RunningLock锁，持锁后，屏幕不会自动灭屏。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-holdRunningLockSync(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      this.context.holdRunningLockSync();
    } catch (err) {
      console.error(`Failed to hold RunningLock. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## notifyDisconnect

```TypeScript
notifyDisconnect(): void
```

通知无障碍服务可以关闭该无障碍扩展服务。

此函数需要与注册预关闭接口  
[on('preDisconnect')](AccessibilityExtensionContext#on(type: 'preDisconnect', callback: Callback&lt;void&gt;))配合使用，如果没有调用过注册预关闭函数，直接调用此函数不生效。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-notifyDisconnect(): void--><!--Device-AccessibilityExtensionContext-notifyDisconnect(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      this.context.notifyDisconnect();
    } catch (err) {
      console.error(`Failed to notify accessibility. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## off('preDisconnect')

```TypeScript
off(type: 'preDisconnect', callback?: Callback<void>): void
```

取消已经向无障碍服务注册的预关闭回调函数，无障碍服务关闭该扩展服务前不再执行该回调。使用callback异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void--><!--Device-AccessibilityExtensionContext-off(type: 'preDisconnect', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'preDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      this.context.off('preDisconnect');
    } catch (err) {
      console.error(`Failed to unRegister. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## on('preDisconnect')

```TypeScript
on(type: 'preDisconnect', callback: Callback<void>): void
```

向无障碍服务注册回调函数，在无障碍服务关闭该无障碍扩展服务前会执行该回调函数。使用callback异步回调。

此注册函数需要与[notifyDisconnect](#notifyDisconnect)配合使用，如果不调用  
[notifyDisconnect](#notifyDisconnect)，则默认等待30秒后，无障碍扩展服务会自动关闭。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void--><!--Device-AccessibilityExtensionContext-on(type: 'preDisconnect', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'preDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      this.context.on('preDisconnect', () => {
        console.info(`To do something before accessibilityExtension disconnect.`);
      });
    } catch (err) {
      console.error(`Failed to register. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

提供拉起前台页面的能力。使用Promise异步回调。

**起始版本：** 12

<!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>--><!--Device-AccessibilityExtensionContext-startAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    let want: Want = {
      bundleName: 'com.huawei.hmos.photos',
      abilityName: 'com.huawei.hmos.photos.MainAbility'
    };

    this.context.startAbility(want).then(() => {
      console.info(`succeeded in starting ability`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to start ability. Code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

## unholdRunningLockSync

```TypeScript
unholdRunningLockSync(): void
```

释放RunningLock锁，恢复自动灭屏。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

<!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void--><!--Device-AccessibilityExtensionContext-unholdRunningLockSync(): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import {
  AccessibilityEvent, 
  AccessibilityExtensionContext
} from '@kit.AccessibilityKit';

export default class AccessibilityManager {
  private static instance: AccessibilityManager;
  context?: AccessibilityExtensionContext;

  static getInstance(): AccessibilityManager {
    if (!AccessibilityManager.instance) {
      AccessibilityManager.instance = new AccessibilityManager();
    }
    return AccessibilityManager.instance;
  }

  onStart(context: AccessibilityExtensionContext) {
    this.context = context;
  }

  onStop() {
    this.context = undefined;
  }

  onEvent(accessibilityEvent: AccessibilityEvent): void {
    if (!this.context) {
      console.error('context is not available!');
      return;
    }

    try {
      this.context.unholdRunningLockSync();
    } catch (err) {
      console.error(`Failed to unhold RunningLock. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```
