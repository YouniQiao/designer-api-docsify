# enable（系统接口）

## enable

```TypeScript
function enable(enable: boolean, callback: AsyncCallback<void>): void
```

开启、关闭键鼠穿越，使用callback异步回调。

> **说明：**
> 
> 从 API version 9开始支持，从API version 23开始废弃。建议使用
> [cooperate.prepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate)、
> [cooperate.unprepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unprepareCooperate)
> 替代。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [prepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate)

<!--Device-inputDeviceCooperate-function enable(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-inputDeviceCooperate-function enable(enable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [enable](#enable) | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
           inputDeviceCooperate.enable(true, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to enable keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in enabling keyboard mouse crossing.`);
            });
          } catch (error) {
            console.error(`Failed to enable keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## enable

```TypeScript
function enable(enable: boolean): Promise<void>
```

开启、关闭键鼠穿越，使用Promise异步回调。

> **说明：**
> 
> 从 API version 9开始支持，从API version 23开始废弃。建议使用
> [cooperate.prepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate)、
> [cooperate.unprepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unprepareCooperate)替代。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [prepareCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate)

<!--Device-inputDeviceCooperate-function enable(enable: boolean): Promise<void>--><!--Device-inputDeviceCooperate-function enable(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [enable](#enable) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          inputDeviceCooperate.enable(true).then(() => {
            console.info(`Succeeded in enabling keyboard mouse crossing.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to enable keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          });
        })
    }
  }
}
```
