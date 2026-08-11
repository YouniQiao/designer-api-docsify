# off（系统接口）

## off('enabledAccessibilityExtensionListChange')

```TypeScript
function off(type: 'enabledAccessibilityExtensionListChange', callback?: Callback<void>): void
```

取消启用的辅助扩展的列表变化监听，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function off(type: 'enabledAccessibilityExtensionListChange', callback?: Callback<void>): void--><!--Device-config-function off(type: 'enabledAccessibilityExtensionListChange', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'enabledAccessibilityExtensionListChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';

let callback = () => {
  console.info('subscribe enabled accessibility extension list change state success');
};
config.on('enabledAccessibilityExtensionListChange', callback);
config.off('enabledAccessibilityExtensionListChange', callback);
```


## off('installedAccessibilityListChange')

```TypeScript
function off(type: 'installedAccessibilityListChange', callback?: Callback<void>): void
```

取消已安装的辅助扩展的列表变化监听，使用callback异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-config-function off(type: 'installedAccessibilityListChange', callback?: Callback<void>): void--><!--Device-config-function off(type: 'installedAccessibilityListChange', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'installedAccessibilityListChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';

let callback = () => {
  console.info('subscribe installed accessibility extension list change state success');
};
config.on('installedAccessibilityListChange', callback);
config.off('installedAccessibilityListChange', callback);
```
