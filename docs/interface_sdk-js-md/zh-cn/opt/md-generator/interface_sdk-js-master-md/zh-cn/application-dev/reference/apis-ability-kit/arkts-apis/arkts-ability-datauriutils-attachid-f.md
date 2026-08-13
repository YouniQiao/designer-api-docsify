# attachId

## attachId

```TypeScript
function attachId(uri: string, id: number): string
```

将ID附加到uri的路径末尾。

**起始版本：** 23

**废弃版本：** -1

<!--Device-dataUriUtils-function attachId(uri: string, id: double): string--><!--Device-dataUriUtils-function attachId(uri: string, id: double): string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 1122;
try {
  let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
    id,
  );
  console.info(`attachId the uri is: ${uri}`);
} catch (err) {
  console.error(`attachId err, code: ${JSON.stringify((err as BusinessError).code)}, msg: ${JSON.stringify((err as BusinessError).message)}`);
}
```
