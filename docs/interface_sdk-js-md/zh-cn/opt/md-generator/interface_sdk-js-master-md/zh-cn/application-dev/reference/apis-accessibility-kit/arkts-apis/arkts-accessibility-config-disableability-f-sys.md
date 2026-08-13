# disableAbility（系统接口）

## disableAbility

```TypeScript
function disableAbility(name: string): Promise<void>
```

关闭辅助扩展。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function disableAbility(name: string): Promise<void>--><!--Device-config-function disableAbility(name: string): Promise<void>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';

config.disableAbility(name).then(() => {
  console.info(`Succeeded in disabling ability, name is ${name}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to disable ability. Code: ${err.code}, message: ${err.message}`);
});
```


## disableAbility

```TypeScript
function disableAbility(name: string, callback: AsyncCallback<void>): void
```

关闭辅助扩展，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

<!--Device-config-function disableAbility(name: string, callback: AsyncCallback<void>): void--><!--Device-config-function disableAbility(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9300001](../errorcode-accessibility.md#9300001-输入无效的包名称或者ability名称) |

## 示例

```TypeScript
import { config } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let name: string = 'com.ohos.example/axExtension';

config.disableAbility(name, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to disable ability. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in disabling, name is ${name}`);
});
```
