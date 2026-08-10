# hasIrEmitter

## 导入模块

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## hasIrEmitter

```TypeScript
function hasIrEmitter(): Promise<boolean>
```

查询设备是否配备红外发射器。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

<!--Device-infraredEmitter-function hasIrEmitter(): Promise<boolean>--><!--Device-infraredEmitter-function hasIrEmitter(): Promise<boolean>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InfraredEmitter

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示设备具有红外发射器；返回false表示设备不具有红外发射器。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 3800001 | Input service exception. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { infraredEmitter } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
            // 查询是否有红外发射器
            infraredEmitter.hasIrEmitter().then((result: boolean) => {
              console.info(`Succeeded in querying infrared emitter: ${JSON.stringify(result)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to query infrared emitter, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`)})
        })
    }
  }
}
```

