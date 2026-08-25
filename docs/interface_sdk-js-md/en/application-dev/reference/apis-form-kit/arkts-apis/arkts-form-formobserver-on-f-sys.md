# on (System API)

## Modules to Import

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## on('formAdd')

```TypeScript
function on(type: 'formAdd', observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of add form. <p>You can use this method to listen to the event of add form.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formAdd' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('formAdd')

```TypeScript
function on(type: 'formAdd', hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of add form. <p>You can use this method to listen to the event of add form for a particular card host.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formAdd' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('formRemove')

```TypeScript
function on(type: 'formRemove', observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of remove form. <p>You can use this method to listen to the event of remove form.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formRemove' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('formRemove')

```TypeScript
function on(type: 'formRemove', hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of remove form. <p>You can use this method to listen to the event of remove form for a particular card host.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formRemove' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('notifyVisible')

```TypeScript
function on(type: 'notifyVisible', observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void
```

Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'notifyVisible' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('notifyVisible')

```TypeScript
function on(
    type: 'notifyVisible',
    hostBundleName: string,
    observerCallback: Callback<Array<formInfo.RunningFormInfo>>
  ): void
```

Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change for a particular card host.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'notifyVisible' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('notifyInvisible')

```TypeScript
function on(type: 'notifyInvisible', observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void
```

Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'notifyInvisible' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('notifyInvisible')

```TypeScript
function on(
    type: 'notifyInvisible',
    hostBundleName: string,
    observerCallback: Callback<Array<formInfo.RunningFormInfo>>,
  ): void
```

Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change for a particular card host.</p>

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'notifyInvisible' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('router')

```TypeScript
function on(type: 'router', observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Router event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'router' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('router')

```TypeScript
function on(type: 'router', hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Router event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'router' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('message')

```TypeScript
function on(type: 'message', observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Message event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'message' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('message')

```TypeScript
function on(type: 'message', hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Message event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'message' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('call')

```TypeScript
function on(type: 'call', observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Call event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'call' | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## on('call')

```TypeScript
function on(type: 'call', hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Call event listening in registered form. <p>This interface requires permission to receive callback.</p>

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'call' | Yes |
| [hostBundleName](arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
