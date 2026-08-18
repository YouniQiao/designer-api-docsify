# start（系统接口）

## 导入模块

```TypeScript
```

## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void
```

启动键鼠穿越，使用callback异步回调。 > **说明：** > > 从 API version 9开始支持，从API version 23开始废弃。建议使用 > [cooperate.activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口) > 替代。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口)

<!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void--><!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinkDeviceDescriptor | string | 是 |
| srcInputDeviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4400002](../errorcode-cooperator.md#4400002-操作输入设备失败) |
| [4400001](../errorcode-cooperator.md#4400001-目标设备描述符错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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
          const sinkDeviceDescriptor = 'descriptor';
          let srcInputDeviceId = 0;
          try {
            inputDeviceCooperate.start(sinkDeviceDescriptor, srcInputDeviceId, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in starting keyboard mouse crossing.`);
            });
          } catch (error) {
            console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## start

```TypeScript
function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>
```

启动键鼠穿越，使用Promise异步回调。 > **说明：** > > 从 API version 9开始支持，从API version 23开始废弃。建议使用 > [cooperate.activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口) > 替代。

**起始版本：** 9

**废弃版本：** 23

**替代接口：** [activateCooperate](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口)

<!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>--><!--Device-inputDeviceCooperate-function start(sinkDeviceDescriptor: string, srcInputDeviceId: number): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sinkDeviceDescriptor | string | 是 |
| srcInputDeviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4400002](../errorcode-cooperator.md#4400002-操作输入设备失败) |
| [4400001](../errorcode-cooperator.md#4400001-目标设备描述符错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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
          const sinkDeviceDescriptor = 'descriptor';
          const srcInputDeviceId = 0;
          inputDeviceCooperate.start(sinkDeviceDescriptor, srcInputDeviceId).then(() => {
            console.info(`Succeeded in starting keyboard mouse crossing.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to start keyboard mouse crossing, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          });
        })
    }
  }
}
```
