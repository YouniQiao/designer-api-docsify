# getTime

## 导入模块

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getTime

```TypeScript
function getTime(isNanoseconds?: boolean): number
```

使用同步方式获取自Unix纪元以来到当前系统时间所经过的时间。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isNanoseconds | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |
