# Config（系统接口）

用于属性的设置、获取与监听。

**起始版本：** 9

<!--Device-config-interface Config<T>--><!--Device-config-interface Config<T>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

## get

```TypeScript
get(): Promise<T>
```

获取属性。使用Promise异步回调。

**起始版本：** 9

<!--Device-Config-get(): Promise<T>--><!--Device-Config-get(): Promise<T>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;T & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

config.highContrastText.get().then((data: boolean) => {
  console.info(`succeeded in getting highContrastText, data is ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get highContrastText. Code: ${err.code}, message: ${err.message}`);
});
```

## get

```TypeScript
get(callback: AsyncCallback<T>): void
```

获取属性，使用callback异步回调。

**起始版本：** 9

<!--Device-Config-get(callback: AsyncCallback<T>): void--><!--Device-Config-get(callback: AsyncCallback<T>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

config.highContrastText.get((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(`Failed to get highContrastText. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in getting highContrastText, data is ${data}`);
});
```

## off

```TypeScript
off(callback?: Callback<T>): void
```

取消属性变化监听，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-Config-off(callback?: Callback<T>): void--><!--Device-Config-off(callback?: Callback<T>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;T&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';

let callback = (data: boolean) => {
  console.info(`subscribe highContrastText success, result: ${JSON.stringify(data)}`);
};
config.highContrastText.on(callback);
config.highContrastText.off(callback);
```

## on

```TypeScript
on(callback: Callback<T>): void
```

添加属性变化监听，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

<!--Device-Config-on(callback: Callback<T>): void--><!--Device-Config-on(callback: Callback<T>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;T&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';

config.highContrastText.on((data: boolean) => {
  console.info(`subscribe highContrastText success, result: ${JSON.stringify(data)}`);
});
```

## set

```TypeScript
set(value: T): Promise<void>
```

设置属性。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-Config-set(value: T): Promise<void>--><!--Device-Config-set(value: T): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let value: boolean = true;

config.highContrastText.set(value).then(() => {
  console.info(`succeeded in setting highContrastText value is ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set highContrastText. Code: ${err.code}, message: ${err.message}`);
});
```

## set

```TypeScript
set(value: T, callback: AsyncCallback<void>): void
```

设置属性，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-Config-set(value: T, callback: AsyncCallback<void>): void--><!--Device-Config-set(value: T, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let value: boolean = true;

config.highContrastText.set(value, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set highContrastText. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`succeeded in setting highContrastText, value is ${value}`);
});
```
