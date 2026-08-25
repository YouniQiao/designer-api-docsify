# updateId

## 导入模块

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
```

## updateId

```TypeScript
function updateId(uri: string, id: double): string
```

更新指定uri中的ID。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| id | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let id = 1122;
  let uri = dataUriUtils.updateId(
    'com.example.dataUriUtils/1221',
    id
  );
  console.info(`update id with the uri is: ${uri}`);
} catch (err) {
  console.error(`update id err, code: ${(err as BusinessError).code}, msg: ${(err as BusinessError).message}`);
}
```
