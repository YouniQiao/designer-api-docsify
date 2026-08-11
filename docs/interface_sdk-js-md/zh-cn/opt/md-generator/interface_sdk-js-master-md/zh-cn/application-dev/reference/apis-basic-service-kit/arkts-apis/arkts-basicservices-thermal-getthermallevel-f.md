# getThermalLevel

## getThermalLevel

```TypeScript
function getThermalLevel(): ThermalLevel
```

获取当前热档位信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [thermal.getLevel](arkts-basicservices-thermal-getlevel-f.md#getlevel)

<!--Device-thermal-function getThermalLevel(): ThermalLevel--><!--Device-thermal-function getThermalLevel(): ThermalLevel-End-->

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 |
| --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) |

## 示例

```TypeScript
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```
