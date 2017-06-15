class Post {
  constructor(title, link, author, img) {
    this.title = title;
    this.author = author;
    this.link = link;
    this.img = img;
  }
}

var VPUdtEf3oXI = new Vue({
  el: '#VPUdtEf3oXI', delimiters: ['[[', ']]'],
	data: {
		randn: Math.random(),
    keyword: 'rgba(127, 127, 127, 0.5)',
    search: '',
		counter: 0,
		onOff: true,
    postList: [
      new Post('Vue.js','https://vuejs.org/','Chris','https://vuejs.org//images/logo.png'),
      new Post('React.js','https://facebook.github.io/react/','Tim','http://daynin.github.io/clojurescript-presentation/img/react-logo.png'),
      new Post('Angular.js','https://angularjs.org/','Sam','https://angularjs.org/img/ng-logo.png'),
      new Post('Ember.js','http://emberjs.com/','Rachel','http://www.gravatar.com/avatar/0cf15665a9146ba852bf042b0652780a?s=200'),
      new Post('Meteor.js','https://www.meteor.com/','Chris','http://hacktivist.in/introduction-to-nodejs-mongodb-meteor/img/meteor.png'),
      new Post('Aurelia','http://aurelia.io/','Tim','https://cdn.auth0.com/blog/aurelia-logo.png'),
      new Post('Node.js','https://nodejs.org/en/','A. A. Ron','https://code-maven.com/img/node.png'),
      new Post('Pusher','https://pusher.com/','Alex','https://avatars1.githubusercontent.com/u/739550?v=3&s=400'),
      new Post('Feathers.js','http://feathersjs.com/','Chuck','https://cdn.worldvectorlogo.com/logos/feathersjs.svg'),
    ],
	},
	methods: {
    styleBox: function() {
      var scale = 100 * Math.random();
  		return {
        'background-color': "green",
        width: scale + 'px',
        height: (scale / 2) + 'px',
      }
    },
		greet: function (event) {
			// `this` inside methods points to the Vue instance
			alert('Hello ' + this.counter + '!')
			// `event` is the native DOM event
			if (event) {
				alert(event.target.tagName)
			}
      this.onOff = !this.onOff;
      this.styleBox();
		},
	},
  computed: {
    filteredList() {
      return this.postList.filter((post) => {
        return post.title.toLowerCase().includes(this.search.toLowerCase());
      });
    }
  }
}).mount;
