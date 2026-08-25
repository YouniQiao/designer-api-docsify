# off（系统接口）

## 导入模块

```TypeScript
import { inputDeviceCooperate } from '@kit.InputKit';
```

## off('cooperation')

```TypeScript
function off(type: 'cooperation', callback?: AsyncCallback<void>): void
```

关闭监听键鼠穿越状态，使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**废弃版本：** 23

**替代接口：** [off](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-cooperate-off-f-sys.md)

**系统能力：** SystemCapability.MultimodalInput.Input.Cooperator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperation' | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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
          // 取消注册单个回调函数
          let callbackOn = (error: BusinessError | undefined, data: { deviceDescriptor: string, eventMsg: EventMsg }) => {
            if (error) {
              console.error(`Failed to monitor cooperation, Code: ${error.code}, message: ${error.message}.`);
              return;
            }
            console.info(`Succeeded in monitoring cooperation, data: ${JSON.stringify(data)}.`);
          };
          try {
            inputDeviceCooperate.on('cooperation', callbackOn);
            inputDeviceCooperate.off('cooperation', callbackOn);
          } catch (error) {
            console.error(`Failed to unregister callback function, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

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
          // 取消注册所有回调函数
          let callback = (error: BusinessError | undefined, data: { deviceDescriptor: string, eventMsg: EventMsg }) => {
            if (error) {
              console.error(`Failed to monitor cooperation, Code: ${error.code}, message: ${error.message}.`);
              return;
            }
            console.info(`Succeeded in monitoring cooperation, data: ${JSON.stringify(data)}.`);
          };
          try {
            inputDeviceCooperate.on('cooperation', callback);
            inputDeviceCooperate.off('cooperation');
          } catch (error) {
            console.error(`Failed to unregister callback function, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
