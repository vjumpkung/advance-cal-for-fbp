var tt=Object.defineProperty;var et=(t,i,e)=>i in t?tt(t,i,{enumerable:!0,configurable:!0,writable:!0,value:e}):t[i]=e;var E=(t,i,e)=>et(t,typeof i!="symbol"?i+"":i,e);import{j as p,M as P,B as q,T as W,a as U,b as ot,d as it,S as st}from"./@mui/material-BQdAtyIz.js";import{c as nt,r as S}from"./vendor-DM_OWPAt.js";import{B as C,Q as rt}from"./react-toastify-6PrFfkGr.js";import{a as H}from"./axios-DXsv3KKR.js";import{F as at}from"./file-saver-B2VyKP5u.js";import{H as lt}from"./react-helmet-D1WOPrvJ.js";import{v as ut}from"./uuid-Ch9TGLTe.js";import{l as f}from"./litegraph.js-CpwqBUsj.js";import{z as l}from"./zod-DXqQCM1T.js";import"./@emotion/react-6hH5lGvJ.js";import"./@emotion/styled-BTak2TOH.js";(function(){const i=document.createElement("link").relList;if(i&&i.supports&&i.supports("modulepreload"))return;for(const s of document.querySelectorAll('link[rel="modulepreload"]'))o(s);new MutationObserver(s=>{for(const u of s)if(u.type==="childList")for(const n of u.addedNodes)n.tagName==="LINK"&&n.rel==="modulepreload"&&o(n)}).observe(document,{childList:!0,subtree:!0});function e(s){const u={};return s.integrity&&(u.integrity=s.integrity),s.referrerPolicy&&(u.referrerPolicy=s.referrerPolicy),s.crossOrigin==="use-credentials"?u.credentials="include":s.crossOrigin==="anonymous"?u.credentials="omit":u.credentials="same-origin",u}function o(s){if(s.ep)return;s.ep=!0;const u=e(s);fetch(s.href,u)}})();var Z,B=nt;Z=B.createRoot,B.hydrateRoot;async function ct(t){const i=t.serialize(),e={};for(const o of t.computeExecutionOrder(!1,0)){const s=i.nodes.find(d=>d.id===o.id);if(o.isVirtualNode){o.applyToGraph&&o.applyToGraph(i);continue}if(o.mode===2||o.mode===4)continue;const u={},n=o.widgets;if(n)for(const d in n){const r=n[d];(!r.options||r.options.serialize!==!1)&&(u[r.name]=r.serializeValue?await r.serializeValue(s,d):r.value)}for(let d in o.inputs){let r=o.getInputNode(d);if(r){let a=o.getInputLink(d);for(;r.mode===4||r.isVirtualNode;){let c=!1;if(r.isVirtualNode)a=r.getInputLink(a.origin_slot),a&&(r=r.getInputNode(a.target_slot),r&&(c=!0));else if(a&&r.mode===4){let h=[a.origin_slot];if(r.inputs){h=h.concat(Object.keys(r.inputs));for(let _ in h)if(_=h[_],r.inputs[_].type===o.inputs[d].type){a=r.getInputLink(_),a&&(r=r.getInputNode(_)),c=!0;break}}}if(!c)break}a&&(u[o.inputs[d].name]=[String(a.origin_id),parseInt(a.origin_slot)])}}e[String(o.id)]={inputs:u,class_type:o.comfyClass}}for(const o in e)for(const s in e[o].inputs)Array.isArray(e[o].inputs[s])&&e[o].inputs[s].length===2&&!e[e[o].inputs[s][0]]&&delete e[o].inputs[s];return{workflow:i,output:e}}const K=ut().toString().replace(/-/gi,"");class dt{constructor(){E(this,"currentExecutingNode",null);E(this,"lastErrorNode",null);E(this,"errorNode",null)}}const L=new dt;function pt(){const t=f.LGraphCanvas.prototype.drawNode,i=f.LGraphCanvas.prototype.drawNodeShape;f.LGraphCanvas.prototype.drawNodeShape=function(e,o,s,u,n,d,r){var g;const a=i.apply(this,arguments),c=(g=L.errorNode)==null?void 0:g[e.id.toString()];let h=null,_=1;if(e.id===+L.currentExecutingNode?h="#0f0":c!=null&&c.errors?(h="red",_=2):L.lastErrorNode&&+L.lastErrorNode.node_id===e.id&&(h="#f0f",_=2),h){const m=e._shape||e.shape||f.LiteGraph.ROUND_SHAPE;o.lineWidth=_,o.globalAlpha=.8,o.beginPath(),m==f.LiteGraph.BOX_SHAPE?o.rect(-6,-6-f.LiteGraph.NODE_TITLE_HEIGHT,12+s[0]+1,12+s[1]+f.LiteGraph.NODE_TITLE_HEIGHT):m==f.LiteGraph.ROUND_SHAPE||m==f.LiteGraph.CARD_SHAPE&&e.flags.collapsed?o.roundRect(-6,-6-f.LiteGraph.NODE_TITLE_HEIGHT,12+s[0]+1,12+s[1]+f.LiteGraph.NODE_TITLE_HEIGHT,this.round_radius*2):m==f.LiteGraph.CARD_SHAPE?o.roundRect(-6,-6-f.LiteGraph.NODE_TITLE_HEIGHT,12+s[0]+1,12+s[1]+f.LiteGraph.NODE_TITLE_HEIGHT,[this.round_radius*2,this.round_radius*2,2,2]):m==f.LiteGraph.CIRCLE_SHAPE&&o.arc(s[0]*.5,s[1]*.5,s[0]*.5+6,0,Math.PI*2),o.strokeStyle=h,o.stroke(),o.strokeStyle=u,o.globalAlpha=1}if(c){o.lineWidth=2,o.strokeStyle="red";for(const m of c.errors)if(m.extra_info&&m.extra_info.input_name){const w=e.findInputSlot(m.extra_info.input_name);if(w!==-1){let x=e.getConnectionPos(!0,w);o.beginPath(),o.arc(x[0]-e.pos[0],x[1]-e.pos[1],12,0,2*Math.PI,!1),o.stroke()}}}return a},f.LGraphCanvas.prototype.drawNode=function(e,o){var s=this.editor_alpha,u=e.bgcolor;e.mode===2&&(this.editor_alpha=.4),e.mode===4&&(e.bgcolor="#FF00FF",this.editor_alpha=.2);const n=t.apply(this,arguments);return this.editor_alpha=s,e.bgcolor=u,n}}let O=null;async function ft(){const t=await H.get("/api/object_info");if(t.status===200)return t.data}async function ht(t){L.errorNode=null;const i=await ct(t),e=await H.post("/api/workflow",{workflow:i.output,client_id:K});if(e.status===200)return await e.data;throw{response:await e.data}}function J(t){if(!O)return O=new WebSocket(`/ws?clientId=${K}`),O.binaryType="arraybuffer",O.addEventListener("open",()=>{t?(console.log("WebSocket Reconnected"),dispatchEvent(new CustomEvent("reconnected"))):console.log("WebSocket Open")}),O.addEventListener("error",()=>{O&&O.close(),console.log("WebSocket Error")}),O.addEventListener("close",()=>{console.log("Reconnecting"),dispatchEvent(new CustomEvent("reconnecting")),setTimeout(()=>{O=null,O=J(!0)},300)}),O.addEventListener("message",i=>{try{const e=JSON.parse(i.data);switch(e.type){case"status":dispatchEvent(new CustomEvent("status",{detail:e.data.status}));break;case"progress":dispatchEvent(new CustomEvent("progress",{detail:e.data}));break;case"executing":dispatchEvent(new CustomEvent("executing",{detail:e.data.node}));break;case"progress":case"executed":case"execution_start":case"execution_success":case"execution_error":case"execution_cached":case"logs":dispatchEvent(new CustomEvent(e.type,{detail:e.data}));break}}catch(e){console.warn("Unhandled message:",i.data,e)}}),O}const M=l.union([l.number().int(),l.string()]),$=l.union([l.object({0:l.number(),1:l.number()}).passthrough().transform(t=>[t[0],t[1]]),l.tuple([l.number(),l.number()])]),gt=l.object({collapsed:l.boolean().optional(),pinned:l.boolean().optional(),allow_interaction:l.boolean().optional(),horizontal:l.boolean().optional(),skip_repeated_outputs:l.boolean().optional()}).passthrough(),A=l.union([l.string(),l.array(l.string()),l.number()]),D=l.union([l.number().int(),l.string().transform(t=>parseInt(t)).refine(t=>!isNaN(t),{message:"Invalid number"})]),mt=l.object({name:l.string(),type:A,link:l.number().nullable().optional(),slot_index:D.optional()}).passthrough(),yt=l.object({name:l.string(),type:A,links:l.array(l.number()).nullable().optional(),slot_index:D.optional()}).passthrough(),_t=l.object({"Node name for S&R":l.string().optional()}).passthrough(),wt=l.union([l.array(l.any()),l.record(l.any())]),bt=l.object({id:M,type:l.string(),pos:$,size:$,flags:gt,order:l.number(),mode:l.number(),inputs:l.array(mt).optional(),outputs:l.array(yt).optional(),title:l.string().optional(),properties:_t,widgets_values:wt.optional(),color:l.string().optional(),bgcolor:l.string().optional()}).passthrough(),xt=l.tuple([l.number(),M,D,M,D,A]),Et=l.object({title:l.string(),bounding:l.tuple([l.number(),l.number(),l.number(),l.number()]),color:l.string().optional(),font_size:l.number().optional(),locked:l.boolean().optional()}).passthrough(),vt=l.object({links_ontop:l.boolean().optional(),align_to_grid:l.boolean().optional()}).passthrough(),Nt=l.object({last_node_id:l.number(),last_link_id:l.number(),nodes:l.array(bt),links:l.array(xt),groups:l.array(Et).optional(),config:vt.optional().nullable(),version:l.number()});function Lt(t){try{const i=JSON.parse(t);return Nt.parse(i)}catch(i){throw i instanceof l.ZodError?console.error("Validation error:",i.errors):console.error("Parsing error:",i),Error(i)}}const kt=(t,i,e,o)=>{var u;const s=(u=o.target.files)==null?void 0:u[0];if(s&&i){L.currentExecutingNode=null,L.errorNode=null,L.lastErrorNode=null;const n=new FileReader;return n.onload=d=>{var r;try{const a=(r=d.target)==null?void 0:r.result,c=Lt(a);i.clear(),i.configure(c),t&&(t.value=""),e.ds.offset=[0,0],e.setZoom(1,[0,0]),e.setDirty(!0,!0),C.success("Loading Workflow Success")}catch{C.error("Error loading workflow file. Please ensure it is a valid workflow.")}},n.onerror=()=>{C.error("Error reading file")},n.readAsText(s),s.name}},St={position:"absolute",top:"50%",left:"50%",transform:"translate(-50%, -50%)",width:"800px",height:"auto",bgcolor:"background.paper",border:"2px solid #000",boxShadow:24,p:4};function It(){const[t,i]=S.useState(!1),e=()=>i(!0),o=()=>i(!1),[s,u]=S.useState({traceback:[],node_id:"",node_type:"",exception_type:"",exception_message:""});return window.addEventListener("execution_error",({detail:n})=>{u(n),e()}),p.jsx("div",{children:p.jsx(P,{open:t,onClose:o,"aria-labelledby":"modal-modal-title","aria-describedby":"modal-modal-description",children:p.jsxs(q,{sx:St,children:[p.jsxs(W,{id:"modal-modal-title",variant:"h5",component:"h2",children:[p.jsx("i",{className:"pi pi-exclamation-triangle",style:{color:"#ff4545"}})," ","Error Workflow Execution"]}),p.jsxs(W,{id:"modal-modal-title",fontFamily:"monospace",children:[s.exception_type," ",p.jsx("br",{})," ",s.exception_message," "]}),p.jsx(W,{id:"modal-modal-description",sx:{mt:2},fontFamily:"monospace",variant:"caption",color:"#828282",children:s.traceback}),p.jsx("div",{style:{display:"flex",justifyContent:"flex-end"},children:p.jsx(U,{onClick:o,children:"Close"})})]})})})}const Ot={position:"absolute",top:"50%",left:"50%",transform:"translate(-50%, -50%)",width:"400px",bgcolor:"background.paper",border:"2px solid #000",boxShadow:24,p:4};function Tt({handleOpen:t,handleClose:i,open:e,invaliddetail:o}){return p.jsx("div",{children:p.jsx(P,{open:e,onClose:i,"aria-labelledby":"modal-modal-title","aria-describedby":"modal-modal-description",children:p.jsxs(q,{sx:Ot,children:[p.jsxs(W,{id:"modal-modal-title",variant:"h5",component:"h2",children:[p.jsx("i",{className:"pi pi-exclamation-circle",style:{color:"#ffc400"}})," ","Invalid Workflow"]}),p.jsxs(W,{id:"modal-modal-description",sx:{mt:2},fontFamily:"monospace",variant:"caption",children:[p.jsx("p",{style:{fontSize:"120%"},children:o.error.message}),Object.keys(o.node_errors).map(s=>p.jsxs("p",{style:{fontSize:"110%"},children:[p.jsxs("span",{style:{fontWeight:"bold"},children:["#",s," ",o.node_errors[s].class_type," :"]}),p.jsx("br",{}),o.node_errors[s].errors.map(u=>p.jsxs("span",{children:[`${u.details} - ${u.message}`,p.jsx("br",{})]},Date.now()+Math.random()))]},Date.now()+Math.random()))]}),p.jsx("div",{style:{display:"flex",justifyContent:"flex-end"},children:p.jsx(U,{onClick:i,children:"Close"})})]})})})}function Ct(){const[t,i]=S.useState(!1);S.useEffect(()=>{t?C.error("Reconnecting",{autoClose:!1}):(C.dismiss(),C.success("Connected to Websocket"))},[t]),window.addEventListener("reconnecting",()=>{t||i(!0)}),window.addEventListener("reconnected",()=>{t&&i(!1)})}function jt({graph:t,canvas:i}){const e=S.useRef(null),[o,s]=S.useState(!1),[u,n]=S.useState(!0),[d,r]=S.useState(null),[a,c]=S.useState("untitled"),[h,_]=S.useState({error:{},node_errors:{}});Ct();const[g,m]=S.useState(!1),w=()=>{var b;(b=e.current)==null||b.click()},x=()=>{if(t){const b=JSON.stringify(t.serialize()),T=new Blob([b],{type:"text/plain;charset=utf-8"}),I=prompt("Enter Filename : ",`workflow-${Date.now()}`);if(I===null)return;at.saveAs(T,`${I}.json`),r(t.serialize()),c(I)}},j=()=>m(!0),z=()=>m(!1),v=()=>{t&&confirm("Clear workflow?")&&(L.currentExecutingNode=null,L.errorNode=null,L.lastErrorNode=null,t.clear(),C.info("Workflow Cleared"),c("untitled"),i.ds.offset=[0,0],i.setZoom(1,[0,0]),i.setDirty(!0,!0))},k=async()=>{try{L.currentExecutingNode=null,L.errorNode=null,L.lastErrorNode=null;const b=await ht(t);t.start(),s(!0)}catch(b){L.errorNode=b.response.data.node_errors,_(b.response.data),m(!0),s(!1)}},y=async()=>{try{await H.post("/api/interrupt",null),await C.warning("Workflow Interrupt")}catch(b){console.error(b)}finally{s(!1)}};window.addEventListener("execution_success",({detail:b})=>{s(!1)}),window.addEventListener("execution_error",({detail:b})=>{s(!1)});const N=ot({palette:{mode:"dark"}});return p.jsxs(p.Fragment,{children:[p.jsx(lt,{children:p.jsxs("title",{children:[u?"":"*",a+" ","- AdvFBP"]})}),p.jsx(it,{theme:N,children:p.jsxs(st,{enableColorScheme:!0,children:[p.jsx(It,{}),p.jsx(Tt,{handleOpen:j,handleClose:z,open:g,invaliddetail:h})]})}),p.jsxs("div",{className:"topbar",children:[p.jsxs("div",{className:"leftmenu",children:[p.jsxs("button",{className:"buttonmenu",onClick:x,children:[p.jsx("i",{className:"pi pi-save"})," Save"]}),p.jsxs("button",{className:"buttonmenu",onClick:w,children:[p.jsx("i",{className:"pi pi-upload"})," Load"]}),p.jsx("input",{type:"file",ref:e,onChange:b=>{const T=kt(e.current,t,i,b);T&&c(T.split(".")[0])},accept:".json",style:{display:"none"}}),p.jsxs("button",{className:"buttonmenu",onClick:v,children:[p.jsx("i",{className:"pi pi-eraser"})," Clear"]})]}),p.jsx("div",{className:"rightmenu",children:p.jsx("button",{className:"buttonmenuright",onClick:async()=>{o?await y():await k()},children:o?p.jsxs("span",{children:[p.jsx("i",{className:"pi pi-stop"})," Interrupt Workflow"]}):p.jsxs("span",{children:[p.jsx("i",{className:"pi pi-play"})," Run Workflow"]})})})]})]})}const R=Symbol(),V=Symbol();function Gt(t,i,e,o,s){function n(r){var g,m;if(t.widgets[0].last_y==null)return;let a=t.widgets[0].last_y,c=r[1]-a,h=0;const _=[];for(let w=0;w<t.widgets.length;w++){const x=t.widgets[w];x.type==="customtext"?_.push(x):x.computeSize?h+=x.computeSize(null)[1]+4:h+=f.LiteGraph.NODE_WIDGET_HEIGHT+4}c-=h,c/=_.length+(((g=t.imgs)==null?void 0:g.length)||0),c<50&&(c=50,t.size[1]=a+h+c*(_.length+(((m=t.imgs)==null?void 0:m.length)||0)),t.graph.setDirtyCanvas(!0));for(const w of t.widgets)w.y=a,w.type==="customtext"?(a+=c,w.computedHeight=c-_.length*4):w.computeSize?a+=w.computeSize()[1]+4:a+=f.LiteGraph.NODE_WIDGET_HEIGHT+4;t.inputHeight=c}const d={type:"customtext",name:i,get value(){return this.inputEl.value},set value(r){this.inputEl.value=r},draw:function(r,a,c,h,_){this.parent.inputHeight||n(t.size);const g=s.ds.scale>.5&&this.type==="customtext",m=10,w=r.canvas.getBoundingClientRect(),x=new DOMMatrix().scaleSelf(w.width/r.canvas.width,w.height/r.canvas.height).multiplySelf(r.getTransform()).translateSelf(m,m+h),j=new DOMMatrix().scaleSelf(x.a,x.d);Object.assign(this.inputEl.style,{transformOrigin:"0 0",transform:j,left:`${x.a+x.e}px`,top:`${x.d+x.f}px`,width:`${c-m*2}px`,height:`${this.parent.inputHeight-m*2}px`,position:"absolute",background:t.color?t.color:"",color:t.color?"white":"",zIndex:o._nodes.indexOf(t)}),this.inputEl.hidden=!g}};if(d.inputEl=document.createElement("textarea"),d.inputEl.className="comfy-multiline-input",d.inputEl.value=e.defaultVal,d.inputEl.placeholder=e.placeholder||"",document.addEventListener("mousedown",function(r){d.inputEl.contains(r.target)||d.inputEl.blur()}),d.parent=t,document.body.appendChild(d.inputEl),t.addCustomWidget(d),s.onDrawBackground=function(){for(let r in o._nodes){const a=o._nodes[r];for(let c in a.widgets){let h=a.widgets[c];Object.hasOwn(h,"inputEl")&&(h.inputEl.style.left="-8000px",h.inputEl.style.position="absolute")}}},t.onRemoved=function(){for(let r in this.widgets)this.widgets[r].inputEl&&this.widgets[r].inputEl.remove()},d.onRemove=()=>{var r;(r=d.inputEl)==null||r.remove(),--t[R]||(t.onResize=t[V],delete t[R],delete t[V])},t[R])t[R]++;else{t[R]=1;const r=t[V]=t.onResize;t.onResize=function(a){n(a),r&&r.apply(this,arguments)}}return{minWidth:400,minHeight:200,widget:d}}function X(t,i){let e=t[1].defaultVal,{min:o,max:s,step:u}=t[1];return e==null&&(e=0),o==null&&(o=-2147483648),s==null&&(s=2147483647),u==null&&(u=i),t[1].min=o,t[1].max=s,t[1].step=u,{val:e,config:{...t[1],precision:4}}}function Q(t){return t==="slider"?"slider":"number"}function zt(t,i,e){let o=Q(e[1].display);const{val:s,config:u}=X(e,10);return Object.assign(u,{precision:0}),{widget:t.addWidget(o,i,s,function(n){const d=this.options.step/10;let r=this.options.min%d;isNaN(r)&&(r=0),this.value=Math.round((n-r)/d)*d+r},u)}}const G={FLOAT(t,i,e){let o=Q(e[1].display),{val:s,config:u}=X(e,.5);return{widget:t.addWidget(o,i,s,()=>{},u)}},INT(t,i,e){return zt(t,i,e)},BOOLEAN(t,i,e){let o=e[1].defaultVal;return{widget:t.addWidget("toggle",i,o,()=>{},{on:e[1].label_on,off:e[1].label_off})}},STRING(t,i,e,o,s){const u=e[1].defaultVal?e[1].defaultVal:"",n=!!e[1].multiline;let d;return n?d=Gt(t,i,e[1],o,s):d={widget:t.addWidget("text",i,u,()=>{},{})},e[1].dynamicPrompts!=null&&(d.widget.dynamicPrompts=e[1].dynamicPrompts),d},COMBO(t,i,e){const o=e[0];let s=o[0];return e[1]&&e[1].defaultVal&&(s=e[1].defaultVal),{widget:t.addWidget("combo",i,s,()=>{},{values:o})}},SELECTFILE(t,i,e,o,s){let u;const n=document.createElement("input");return Object.assign(n,{type:"file",style:"display: none",onchange:async()=>{if(n.files.length){const d=n.files[0],r=new FormData;r.append("file",d);const a=await H.post("/api/upload/file",r);if(a.status!==200){console.error(a.data);return}t.widgets[0].value=a.data.path,n.value=""}}}),document.body.append(n),u=t.addWidget("button","Select File","file",()=>{n.click()}),t.onRemoved=function(){n.remove()},u.serialize=!1,{widget:u}}};async function Rt(t,i){class e{constructor(){E(this,"properties");E(this,"serialize_widgets");E(this,"isVirtualNode");E(this,"color",f.LGraphCanvas.node_colors.yellow.color);E(this,"bgcolor",f.LGraphCanvas.node_colors.yellow.bgcolor);E(this,"groupcolor",f.LGraphCanvas.node_colors.yellow.groupcolor);this.properties||(this.properties={},this.properties.text=""),G.STRING(this,"",["",{defaultVal:this.properties.text,multiline:!0}],t,i),this.serialize_widgets=!0,this.isVirtualNode=!0}}E(e,"category"),f.LiteGraph.registerNodeType("Note",Object.assign(e,{title_mode:f.LiteGraph.NORMAL_TITLE,title:"Note",collapsable:!0})),e.category="utils"}async function Wt(t,i){const o=class o{constructor(){E(this,"size");E(this,"__outputType");E(this,"inputs");E(this,"outputs");E(this,"isVirtualNode");E(this,"horizontal");E(this,"properties");this.properties||(this.properties={}),this.properties.showOutputText=o.defaultVisibility,this.properties.horizontal=!1;const u=this;u.addInput("","*"),u.addOutput(this.properties.showOutputText?"*":"","*"),u.onConnectionsChange=function(n,d,r,a){var z;if(this.applyOrientation(),r&&n===f.LiteGraph.OUTPUT&&new Set(this.outputs[0].links.map(k=>t.links[k].type).filter(k=>k!=="*")).size>1){const k=[];for(let y=0;y<this.outputs[0].links.length-1;y++){const N=this.outputs[0].links[y],b=t.links[N];k.push(b)}for(const y of k)t.getNodeById(y.target_id).disconnectInput(y.target_slot)}let c=this,h=[],_=null,g=null;for(;c;){h.unshift(c);const v=c.inputs[0].link;if(v!==null){const k=t.links[v],y=t.getNodeById(k.origin_id);if(y.constructor.type==="Reroute")y===this?(c.disconnectInput(k.target_slot),c=null):c=y;else{g=c,_=((z=y.outputs[k.origin_slot])==null?void 0:z.type)??null;break}}else{c=null;break}}const m=[this];let w=null;for(;m.length;){c=m.pop();const v=(c.outputs?c.outputs[0].links:[])||[];if(v.length)for(const k of v){const y=t.links[k];if(!y)continue;const N=t.getNodeById(y.target_id);if(N.constructor.type==="Reroute")m.push(N),h.push(N);else{const T=N.inputs&&N.inputs[y==null?void 0:y.target_slot]&&N.inputs[y.target_slot].type?N.inputs[y.target_slot].type:null;_&&T!==_?N.disconnectInput(y.target_slot):w=T}}}const x=_||w||"*",j=f.LGraphCanvas.link_type_colors[x];for(const v of h){v.outputs[0].type=_||"*",v.__outputType=x,v.outputs[0].name=v.properties.showOutputText?x:"",v.size=v.computeSize(),v.applyOrientation();for(const k of v.outputs[0].links||[]){const y=t.links[k];y&&(y.color=j)}}if(g){const v=t.links[g.inputs[0].link];v&&(v.color=j)}},this.clone=function(){const n=o.prototype.clone.apply(this);return n.removeOutput(0),n.addOutput(this.properties.showOutputText?"*":"","*"),n.size=n.computeSize(),n},this.isVirtualNode=!0}getExtraMenuOptions(u,n){n.unshift({content:(this.properties.showOutputText?"Hide":"Show")+" Type",callback:()=>{this.properties.showOutputText=!this.properties.showOutputText,this.properties.showOutputText?this.outputs[0].name=this.__outputType||this.outputs[0].type:this.outputs[0].name="",this.size=this.computeSize(),this.applyOrientation(),t.setDirtyCanvas(!0,!0)}},{content:(o.defaultVisibility?"Hide":"Show")+" Type By Default",callback:()=>{o.setDefaultTextVisibility(!o.defaultVisibility)}},{content:"Set "+(this.properties.horizontal?"Horizontal":"Vertical"),callback:()=>{this.properties.horizontal=!this.properties.horizontal,this.applyOrientation()}})}applyOrientation(){this.horizontal=this.properties.horizontal,this.horizontal?this.inputs[0].pos=[this.size[0]/2,0]:delete this.inputs[0].pos,t.setDirtyCanvas(!0,!0)}computeSize(){return[this.properties.showOutputText&&this.outputs&&this.outputs.length?Math.max(75,f.LiteGraph.NODE_TEXT_SIZE*this.outputs[0].name.length*.6+40):75,26]}clone(){}static setDefaultTextVisibility(u){o.defaultVisibility=u,u?localStorage["Comfy.RerouteNode.DefaultVisibility"]="true":delete localStorage["Comfy.RerouteNode.DefaultVisibility"]}};E(o,"category"),E(o,"defaultVisibility");let e=o;e.setDefaultTextVisibility(!!localStorage["Comfy.RerouteNode.DefaultVisibility"]),f.LiteGraph.registerNodeType("Reroute",Object.assign(e,{title_mode:f.LiteGraph.NO_TITLE,title:"Reroute",collapsable:!1})),e.category="utils"}async function Ht(t,i,e){const o=a=>Object.keys(a).sort().reduce((c,h)=>(c[h]=a[h],c),{});function s(){var a=[];const c=t;for(const _ in c){const g=c[_];var h=g.input.required;g.input.optional!==void 0&&(h=Object.assign({},g.input.required,g.input.optional));for(const m in h){const x=h[m][0];Array.isArray(x)||a.push(x)}for(const m in g.output){const w=g.output[m];a.push(w)}}return a}function u(a){var c=s();for(const h of c)a.colors.node_slot[h]||(a.colors.node_slot[h]="");return a.colors.node_slot=o(a.colors.node_slot),a}const n=async a=>{if(a=await u(a),a.colors){if(a.colors.node_slot&&(Object.assign(e.default_connection_color_byType,a.colors.node_slot),Object.assign(f.LGraphCanvas.link_type_colors,a.colors.node_slot)),a.colors.litegraph_base){e.node_title_color=a.colors.litegraph_base.NODE_TITLE_COLOR,e.default_link_color=a.colors.litegraph_base.LINK_COLOR;for(const c in a.colors.litegraph_base)a.colors.litegraph_base.hasOwnProperty(c)&&f.LiteGraph.hasOwnProperty(c)&&(f.LiteGraph[c]=a.colors.litegraph_base[c])}e.draw(!0,!0)}};let r=await(await H.get("/api/color_palette")).data.dark;await n(r)}function Dt(){f.LiteGraph.search_filter_enabled=!1,f.LiteGraph.middle_click_slot_add_default_node=!0}async function Vt(t,i,e){var a;var o=i.name;const s=(a=i.input)==null?void 0:a.required;for(const c in s){var u=s[c];if(typeof u[0]!="string")continue;var n=u[0];if(n in G){var d=u[1];if(!(d!=null&&d.forceInput))continue}if(n in e.slot_types_default_out||(e.slot_types_default_out[n]=["Reroute"]),e.slot_types_default_out[n].includes(o))continue;e.slot_types_default_out[n].push(o);const h=n.toLocaleLowerCase();h in f.LiteGraph.registered_slot_in_types||(f.LiteGraph.registered_slot_in_types[h]={nodes:[]}),f.LiteGraph.registered_slot_in_types[h].nodes.push(t.comfyClass)}var r=i.output;for(const c in r){var n=r[c];n in e.slot_types_default_in||(e.slot_types_default_in[n]=["Reroute"]),e.slot_types_default_in[n].push(o),n in f.LiteGraph.registered_slot_out_types||(f.LiteGraph.registered_slot_out_types[n]={nodes:[]}),f.LiteGraph.registered_slot_out_types[n].nodes.push(t.comfyClass),f.LiteGraph.slot_types_out.includes(n)||f.LiteGraph.slot_types_out.push(n)}f.LiteGraph.slot_types_default_out={},f.LiteGraph.slot_types_default_in={};for(const c in e.slot_types_default_out)f.LiteGraph.slot_types_default_out[c]=e.slot_types_default_out[c].slice(0,5);for(const c in e.slot_types_default_in)f.LiteGraph.slot_types_default_in[c]=e.slot_types_default_in[c].slice(0,5)}async function Mt(t,i,e){await Rt(i,e),await Wt(i),await Ht(t,i,e)}async function At(t,i,e){await Dt()}function Ft(t){if(t==null)return"(unknown error)";const i=t.traceback.join("");return t.node_id,`Error occurred when executing ${t.node_type}:

${t.exception_message}

${i}`}function Bt(t,i){window.addEventListener("status",({detail:e})=>{console.log("status",e)}),window.addEventListener("reconnecting",()=>{console.log("Reconnecting...")}),window.addEventListener("progress",({detail:e})=>{i.setDirtyCanvas(!0,!1)}),window.addEventListener("executing",({detail:e})=>{L.currentExecutingNode=e,i.setDirtyCanvas(!0,!1)}),window.addEventListener("executed",({detail:e})=>{L.currentExecutingNode=null;const o=i.getNodeById(e.node);o&&o.onExecuted&&o.onExecuted(e.output)}),window.addEventListener("execution_start",({detail:e})=>{L.lastErrorNode=null,C.info("Workflow Start")}),window.addEventListener("execution_success",({detail:e})=>{C.info("Workflow Execution Success"),i.stop()}),window.addEventListener("execution_error",({detail:e})=>{const o=Ft(e);L.lastErrorNode=e,L.currentExecutingNode=null,i.stop(),console.error(o)})}async function $t(t){var i,e,o,s;((s=(o=(e=(i=t==null?void 0:t.input)==null?void 0:i.required)==null?void 0:e.path)==null?void 0:o[1])==null?void 0:s.select_file_path)===!0&&(t.input.required.selectfile=["SELECTFILE"])}async function Pt(t,i,e,o){if(i.name==="ShowText"){let s=function(u){var n,d;if(this.widgets){const r=this.widgets.findIndex(a=>a.name==="text");if(r!==-1){for(let a=r;a<this.widgets.length;a++)(d=(n=this.widgets[a]).onRemove)==null||d.call(n);this.widgets.length=r}}for(const r of u){const a=G.STRING(this,"text",["STRING",{multiline:!0}],e,o).widget;a.inputEl.readOnly=!0,a.inputEl.style.opacity=1,a.value=r}requestAnimationFrame(()=>{var a;const r=this.computeSize();r[0]<this.size[0]&&(r[0]=this.size[0]),r[1]<this.size[1]&&(r[1]=this.size[1]),(a=this.onResize)==null||a.call(this,r),e.setDirtyCanvas(!0,!1)})};t.onExecuted,t.prototype.onExecuted=function(u){s.call(this,u.text)}}}async function qt(t,i,e){var s;const o={slot_types_default_out:{},slot_types_default_in:{}};for(const u in t){const n=t[u];await $t(n);const d=(s=class extends f.LGraphNode{constructor(c){var w,x,j,z,v,k;super(c);E(this,"comfyClass",n.name);E(this,"graph",i);E(this,"canvas",e);const h=n.input.required;var _=n.input.required;n.input.optional!=null&&(_=Object.assign({},n.input.required,n.input.optional));const g={minWidth:1,minHeight:1};for(const y in _){const N=_[y],b=N[0],T=N[1]??{},I=[b,T],Y=h&&y in h;let F=!0;(w=I[1])!=null&&w.forceInput?this.addInput(y,b):Array.isArray(b)?Object.assign(g,G.COMBO(this,y,I)||{}):`${b}:${y}`in G?Object.assign(g,G[`${b}:${y}`](this,y,I,this.graph,this.canvas)||{}):b in G?Object.assign(g,G[b](this,y,I,this.graph,this.canvas)||{}):(this.addInput(y,b),F=!1),F&&(g!=null&&g.widget)&&((x=g.widget).options??(x.options={}),Y||(g.widget.options.inputIsOptional=!0),(j=I[1])!=null&&j.forceInput&&(g.widget.options.forceInput=!0),(z=I[1])!=null&&z.defaultInput&&(g.widget.options.defaultInput=!0),(v=I[1])!=null&&v.advanced&&(g.widget.advanced=!0),(k=I[1])!=null&&k.hidden&&(g.widget.hidden=!0))}for(const y in n.output){let N=n.output[y];N instanceof Array&&(N="COMBO");const b=n.output_name[y]||N,I={shape:n.output_is_list[y]?f.LiteGraph.GRID_SHAPE:f.LiteGraph.CIRCLE_SHAPE};this.addOutput(b,N,I)}const m=this.computeSize();m[0]=Math.max(g.minWidth,m[0]*1.5),m[1]=Math.max(g.minHeight,m[1]),this.size=m,this.serialize_widgets=!0}configure(c){const h=(_,g)=>{const m={...g};if(_.widget===void 0&&g.widget!==void 0)return this.inputs.push(_),g;for(const w of["name","type","shape"])_[w]!==void 0&&(m[w]=_[w]);return m};for(const _ of["inputs","outputs"]){const g=c[_]??[];c[_]=g.map((m,w)=>h(this[_][w]??{},m))}super.configure(c)}},E(s,"title",n.display_name?n.display_name:n.name),E(s,"nodeData",n),E(s,"category"),s);await Pt(d,n,i,e),await Vt(d,n,o),f.LiteGraph.registerNodeType(u,d),d.category=n.category}}async function Ut(t,i,e){const o=new f.LGraph,s=new f.LGraphCanvas(t,o);function u(){const d=Math.max(window.devicePixelRatio,1),{width:r,height:a}=t.getBoundingClientRect();t.width=Math.round(r*d),t.height=Math.round(a*d),t.getContext("2d").scale(d,d),s.draw(!0,!0)}u(),window.addEventListener("resize",u),f.LiteGraph.release_link_on_empty_shows_menu=!0,f.LiteGraph.alt_drag_do_clone_nodes=!0,f.LiteGraph.clearRegisteredTypes();const n=await ft();await At(),await qt(n,o,s),await Mt(n,o,s),J(!1),Bt(s,o),pt(),i(o),e(s)}function Zt({setGraph:t,setCanvas:i,canvasRef:e}){S.useEffect(()=>{e.current&&Ut(e.current,t,i)},[])}function Kt(){const t=S.useRef(null),[i,e]=S.useState(void 0),[o,s]=S.useState(void 0);return Zt({setGraph:e,setCanvas:s,canvasRef:t}),p.jsxs(p.Fragment,{children:[p.jsx(jt,{graph:i,canvas:o}),p.jsx("canvas",{style:{position:"absolute",zIndex:0,touchAction:"none"},ref:t,id:"graph-canvas"})]})}Z(document.getElementById("root")).render(p.jsxs(p.Fragment,{children:[p.jsx(Kt,{}),p.jsx(rt,{style:{marginTop:"1.25em"},position:"top-right",autoClose:5e3,pauseOnHover:!1,draggable:!1,hideProgressBar:!0,theme:"colored"})]}));
