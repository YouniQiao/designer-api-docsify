# InvocationHandler

Interface for handling method invocations on a proxy object. Defines methods to manage property access, assignment, and method invocation.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## get

```TypeScript
get(proxy: Proxy, method: InstanceMethod): Any
```

Intercepts the getter operation for the each property on the proxy object.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | Yes |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Any |

## invoke

```TypeScript
invoke(proxy: Proxy, method: InstanceMethod, args: FixedArray<Any>): Any
```

Intercepts invocation of a method on the proxy object with the provided arguments.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | Yes |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Any |

## set

```TypeScript
set(proxy: Proxy, method: InstanceMethod, value: Any): void
```

Intercepts the setter operation of a method on the proxy object.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [Proxy](arkts-arkts-reflect-proxy-c.md) | Yes |
| method | [InstanceMethod](arkts-arkts-reflect-instancemethod-c.md) | Yes |
| value | Any | Yes |
