# createZip

## 导入模块

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## createZip

```TypeScript
function createZip(): Promise<Zip>
```

创建压缩解压缩对象实例。使用Promise异步回调。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Zip](arkts-basicservices-zlib-zip-i.md)&gt; |
