<!-- fontawesome 사이트의 CSS사용하기 : 
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">



 <div class="flex justify-between">
        <div>
            #supoerhost인 경우에만 superhost를 표기하기.
            {% if room.host.superhost %}
                <span class="mr-pk uppercase font-medium text-xs border border-black text-black rounded py-px px-1">superhost</span>
            {% endif %}
                
            <span class="text-sm text-green-600">{{room.city}}</span>
        </div>
        #구분할때 div대신 sapn을 사용해도 된다.
        <span class="text-sm flex items-center">
            <i class="fas fa-star text-red-500 text-xs mr-1"></i>{{room.total_rating}}
        </span>
</div> -->
