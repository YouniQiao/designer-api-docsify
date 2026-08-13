# @ohos.app.form.formObserver

Interface of formObserver.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace formObserver--><!--Device-unnamed-declare namespace formObserver-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getRunningFormInfoById) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getRunningFormInfoById-(System-API)) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getRunningFormInfoById-(System-API)) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getRunningFormInfoById-(System-API)) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getRunningFormInfos) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getRunningFormInfos-(System-API)) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getRunningFormInfos-(System-API)) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getRunningFormInfos-(System-API)) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getRunningFormInfosByFilter) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getRunningFormInfosByFilter-(System-API)) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [offCall](arkts-form-formobserver-offcall-f-sys.md#offCall) | Unregister form call event Listening. |
| [offFormAdd](arkts-form-formobserver-offformadd-f-sys.md#offFormAdd) | Cancels listening to the event of add form. &lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| [offFormRemove](arkts-form-formobserver-offformremove-f-sys.md#offFormRemove) | Cancels listening to the event of remove form. &lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| [offMessage](arkts-form-formobserver-offmessage-f-sys.md#offMessage) | Unregister form message event Listening. |
| [offNotifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offNotifyInvisible) | Cancels listening to the event of notifyInvisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| [offNotifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offNotifyVisible) | Cancels listening to the event of notifyVisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| [offRouter](arkts-form-formobserver-offrouter-f-sys.md#offRouter) | Unregister form router event Listening. |
| off_call | Unregister form call event Listening. |
| off_formAdd | Cancels listening to the event of add form. &lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| off_formRemove | Cancels listening to the event of remove form. &lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| off_message | Unregister form message event Listening. |
| off_notifyInvisible | Cancels listening to the event of notifyInvisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| off_notifyVisible | Cancels listening to the event of notifyVisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| off_router | Unregister form router event Listening. |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#onCall) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#onCall-(System-API)) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onFormAdd) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onFormAdd-(System-API)) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onFormRemove) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onFormRemove-(System-API)) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onMessage) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onMessage-(System-API)) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onNotifyInvisible) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onNotifyInvisible-(System-API)) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onNotifyVisible) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onNotifyVisible-(System-API)) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onRouter) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onRouter-(System-API)) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| on_call | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_call](arkts-form-formobserver-oncall-f-sys.md#on_call-1) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| on_formAdd | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md#on_formadd-1) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| on_formRemove | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md#on_formremove-1) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| on_message | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md#on_message-1) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| on_notifyInvisible | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#on_notifyinvisible-1) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| on_notifyVisible | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#on_notifyvisible-1) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| on_router | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md#on_router-1) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
<!--DelEnd-->

