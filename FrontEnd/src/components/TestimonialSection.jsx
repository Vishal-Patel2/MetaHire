import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";
import { Quote } from "lucide-react";

const testimonials = [
  {
    name: "Anup Yadav",
    role: "Software Engineer at Microsoft",
    content:
      "MetaHire's AI mock interviews helped me prepare for tough technical questions. The personalized feedback was invaluable in landing my dream job.",
    avatar:
      "https://www.gniotgroup.edu.in/latestnews/1711701147-1.jpg",
  },
  {
    name: "Rishav Yadav",
    role: "System Engineer at TCS",
    content:
      "The resume analysis feature gave me insights I never would have considered. It completely transformed my approach to interviews.",
    avatar:
      "https://media.licdn.com/dms/image/v2/D5603AQEwovvnL-tX8Q/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1707755946672?e=2147483647&v=beta&t=v2DFv39IDJD8NuJXEhv-DMs_XpzZyKSaR-wH-4QmaDI",
  },
  {
    name: "Sachindra Patel",
    role: "Software Engineer at Tealium CDP",
    content:
      "The domain-specific questions were spot-on. MetaHire helped me gain confidence and improve my technical communication skills.",
    avatar:
      "https://media.licdn.com/dms/image/v2/D4D03AQH7ez59ovGX7w/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1694972916773?e=1744243200&v=beta&t=iek16m7-q2D5dr2zTOyqL-fnuDfrNOzFLO8QxXj6j4w",
  },
];

const TestimonialSection = () => {
  return (
    <section className="py-16   my-20 font-mainFont">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-5xl font-bold text-blue-600">
            Success Stories
          </h2>
          <p className="text-lg lg:text-xl text-gray-300 mt-4">
            Hear from professionals who transformed their interview experience
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.2 }}
            >
              <Card className="bg-black bg-opacity-50 border-none shadow-lg shadow-blue-700 h-full">
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    <img
                      src={testimonial.avatar}
                      alt={testimonial.name}
                      className="w-12 h-12 rounded-full mr-4"
                    />
                    <div>
                      <h3 className="text-blue-300 font-semibold">
                        {testimonial.name}
                      </h3>
                      <p className="text-gray-400 text-sm">
                        {testimonial.role}
                      </p>
                    </div>
                  </div>
                  <div className="relative">
                    {/* <Quote className="absolute -top-2 -left-2 w-8 h-8 text-blue-600/20" /> */}
                    <p className="text-gray-300 relative z-10 pl-6">
                      "{testimonial.content}"
                    </p>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialSection;
